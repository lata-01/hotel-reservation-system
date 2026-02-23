import sqlite3

def init_db():
    conn = sqlite3.connect("restaurant.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hotels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        location TEXT,
        max_capacity INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        restaurant_name TEXT,
        date TEXT,
        start_time TEXT,
        end_time TEXT,
        number_of_person INTEGER,
        user_name TEXT,
        mobile_number TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS waiting_list (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        restaurant_name TEXT,
        date TEXT,
        start_time TEXT,
        end_time TEXT,
        number_of_person INTEGER,
        user_name TEXT,
        mobile_number TEXT
    )
    """)

    conn.commit()
    conn.close()


def get_connection():
    return sqlite3.connect("restaurant.db")
