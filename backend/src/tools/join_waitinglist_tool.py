from typing import Type, Any, Dict, List

from pydantic import BaseModel, Field
from langchain_core.tools import BaseTool
from src.db.database import get_connection


class JoinWaitingListToolInput(BaseModel):
    restaurant_name: str = Field(description="Name of the restaurant")
    date: str = Field(description="Reservation date, format dd/mm/yyyy")
    time_window: List[str] = Field(
        description="Reservation time window, start time, end time, end time can be 00:00, format hh:mm"
    )
    number_of_person: int = Field(
        description="Number of people to book reservation for"
    )
    user_name: str = Field(description="Name of the user")
    mobile_number: str = Field(description="Mobile number of the user")


class JoinWaitingListTool(BaseTool):
    name: str = "join_waiting_list"
    description: str = "Save user in real waiting list"
    args_schema: Type[BaseModel] = JoinWaitingListToolInput

    def _run(self, **kwargs):
        args = JoinWaitingListToolInput.model_validate(kwargs)

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO waiting_list 
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

        cursor.execute("SELECT COUNT(*) FROM waiting_list WHERE LOWER(restaurant_name)=LOWER(?) AND date=?")
        position = cursor.fetchone()[0]

        conn.close()

        return f"You are added to waiting list. Position: {position}"
