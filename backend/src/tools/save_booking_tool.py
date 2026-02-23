from typing import Type, Any, Dict, List

from pydantic import BaseModel, Field
from langchain_core.tools import BaseTool

from src import logging
from src.db.database import get_connection
import uuid
from src.db.database import get_connection

logger = logging.getLogger(__name__)


class SaveBookingToolInput(BaseModel):
    restaurant_name: str = Field(
        description="Name of the restaurant to get table information"
    )
    date: str = Field(description="Reservation date, format dd/mm/yyyy")
    time_window: List[str] = Field(
        description="Reservation time window, start time, end time, end time can be 00:00, format hh:mm"
    )
    number_of_person: int = Field(
        description="Number of people to book reservation for"
    )
    user_name: str = Field(description="Name of the user")
    mobile_number: str = Field(description="Mobile number of the user")
    confirm_partial: bool = Field(
    default=False,
    description="User confirmation to book fewer seats if full capacity not available"
)



class SaveBookingTool(BaseTool):
    name: str = "save_booking"
    description: str = "Save booking if capacity allows"
    args_schema: Type[BaseModel] = SaveBookingToolInput

    def _run(self, **kwargs):
        args = SaveBookingToolInput.model_validate(kwargs)

        conn = get_connection()
        cursor = conn.cursor()

        # 🔹 Check hotel exists
        cursor.execute("""
            SELECT max_capacity FROM hotels
            WHERE LOWER(name)=LOWER(?)
        """, (args.restaurant_name.strip(),))

        hotel = cursor.fetchone()

        if hotel is None:
            # Fetch available hotels
            cursor.execute("SELECT name FROM hotels")
            hotels = [row[0] for row in cursor.fetchall()]
            conn.close()

            if hotels:
                hotel_list = "\n".join(f"- {h}" for h in hotels)
                return (
                    f"❌ '{args.restaurant_name}' is not registered.\n\n"
                    f"Available hotels:\n{hotel_list}"
                )
            else:
                return "❌ No hotels registered in system."

        max_capacity = hotel[0]

        # 🔹 Check overlapping bookings
        cursor.execute("""
            SELECT SUM(number_of_person) FROM bookings
            WHERE LOWER(restaurant_name)=LOWER(?)
            AND date=?
            AND start_time < ?
            AND end_time > ?
        """, (
            args.restaurant_name,
            args.date,
            args.time_window[1],  # new_end
            args.time_window[0],  # new_start
        ))

        result = cursor.fetchone()[0]
        booked = result if result else 0

        available = max_capacity - booked

        # 🔹 Capacity check
        if available < args.number_of_person:
            if available > 0 and args.confirm_partial:
                args.number_of_person = available
            else:
                conn.close()
                return (
                    f"❌ Only {available} seats available at {args.restaurant_name}. "
                    f"Would you like to book {available} seats or join waiting list?"
                )


        # 🔹 Insert booking (using restaurant_name)
        cursor.execute("""
            INSERT INTO bookings
            (restaurant_name, date, start_time, end_time,
             number_of_person, user_name, mobile_number)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            args.restaurant_name,
            args.date,
            args.time_window[0],
            args.time_window[1],
            args.number_of_person,
            args.user_name,
            args.mobile_number,
        ))

        conn.commit()
        conn.close()

        return f"✅ Booking confirmed at {args.restaurant_name}!"
