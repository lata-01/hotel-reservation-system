from typing import Type, Any, Dict, List
from random import random

from pydantic import BaseModel, Field
from langchain_core.tools import BaseTool
from src.db.database import get_connection


class GetTableAvailabilityToolInput(BaseModel):
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


class GetTableAvailabilityTool(BaseTool):
    name: str = "get_table_availability"
    description: str = "Check availability from database"
    args_schema: Type[BaseModel] = GetTableAvailabilityToolInput

    def _run(self, **kwargs):
        args = GetTableAvailabilityToolInput.model_validate(kwargs)

        conn = get_connection()
        cursor = conn.cursor()

        # 🔹 Check hotel exists (case-insensitive)
        cursor.execute("""
            SELECT max_capacity FROM hotels
            WHERE LOWER(name)=LOWER(?)
        """, (args.restaurant_name.strip(),))

        hotel = cursor.fetchone()

        if not hotel:
            # Fetch all available hotels
            cursor.execute("""
                SELECT name, location FROM hotels
            """)
            hotels = cursor.fetchall()

            conn.close()

            if not hotels:
                return "❌ No hotels are currently registered in the system."

            hotel_list = "\n".join(
                f"- {name} ({location})"
                for name, location in hotels
            )

            return (
                f"❌ '{args.restaurant_name}' is not registered.\n\n"
                f"Available hotels:\n{hotel_list}"
            )

        max_capacity = hotel[0]

        # 🔹 Check overlapping bookings using restaurant_name
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

        conn.close()

        if available >= args.number_of_person:
            return f"✅ {available} seats available."
        elif available > 0:
            return f"⚠ Only {available} seats available."
        else:
            return "❌ No seats available."
