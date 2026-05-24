# import sqlite3
# from pathlib import Path


# DB_PATH = Path("data/houses.db")


# def create_connection():
#     Path("data").mkdir(exist_ok=True)
#     return sqlite3.connect(DB_PATH)


# def create_table():
#     conn = create_connection()
#     cursor = conn.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS houses (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT,
#             total_area REAL,
#             living_area REAL,
#             floors INTEGER,
#             bedrooms INTEGER,
#             dimensions TEXT,
#             price INTEGER,
#             url TEXT UNIQUE
#         )
#     """)

#     conn.commit()
#     conn.close()

#     print("✅ Table created")


# # НОРМАЛИЗАЦИЯ ДАННЫХ 
# def normalize(house: dict):
#     def to_float(x):
#         if not x:
#             return None
#         return float(str(x).replace(" м2", "").replace(",", ".").strip())

#     def to_int(x):
#         if not x:
#             return None
#         return int(str(x).replace(" ", "").strip())

#     return {
#         "title": house.get("title"),
#         "total_area": to_float(house.get("total_area")),
#         "living_area": to_float(house.get("living_area")),
#         "floors": int(house.get("floors")) if house.get("floors") else None,
#         "bedrooms": int(house.get("bedrooms")) if house.get("bedrooms") else None,
#         "dimensions": house.get("dimensions"),
#         "price": to_int(house.get("price")),
#         "url": house.get("url"),
#     }


# def insert_house(house: dict):
#     conn = create_connection()
#     cursor = conn.cursor()

#     h = normalize(house)

#     cursor.execute("""
#         INSERT OR IGNORE INTO houses (
#             title,
#             total_area,
#             living_area,
#             floors,
#             bedrooms,
#             dimensions,
#             price,
#             url
#         )
#         VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#     """, (
#         h["title"],
#         h["total_area"],
#         h["living_area"],
#         h["floors"],
#         h["bedrooms"],
#         h["dimensions"],
#         h["price"],
#         h["url"]
#     ))

#     conn.commit()
#     conn.close()


# def save_houses(houses: list):
#     for house in houses:
#         insert_house(house)

#     print(f"💾 Saved {len(houses)} houses to database")

import psycopg2


DB_CONFIG = {
    "host": "postgres_db",
    "database": "scraper_db",
    "user": "admin",
    "password": "secret"
}


def create_connection():
    return psycopg2.connect(**DB_CONFIG)


def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS houses (
            id SERIAL PRIMARY KEY,
            title TEXT,
            total_area REAL,
            living_area REAL,
            floors INTEGER,
            bedrooms INTEGER,
            dimensions TEXT,
            price INTEGER,
            url TEXT UNIQUE
        )
    """)

    conn.commit()
    conn.close()

    print("✅ PostgreSQL table created")


def normalize(house: dict):

    def to_float(x):
        if not x:
            return None

        return float(
            str(x)
            .replace(" м2", "")
            .replace(",", ".")
            .strip()
        )

    def to_int(x):
        if not x:
            return None

        return int(
            str(x)
            .replace(" ", "")
            .strip()
        )

    return {
        "title": house.get("title"),
        "total_area": to_float(house.get("total_area")),
        "living_area": to_float(house.get("living_area")),
        "floors": int(house.get("floors")) if house.get("floors") else None,
        "bedrooms": int(house.get("bedrooms")) if house.get("bedrooms") else None,
        "dimensions": house.get("dimensions"),
        "price": to_int(house.get("price")),
        "url": house.get("url"),
    }


def insert_house(house: dict):

    conn = create_connection()
    cursor = conn.cursor()

    h = normalize(house)

    cursor.execute("""
        INSERT INTO houses (
            title,
            total_area,
            living_area,
            floors,
            bedrooms,
            dimensions,
            price,
            url
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (url) DO NOTHING
    """, (
        h["title"],
        h["total_area"],
        h["living_area"],
        h["floors"],
        h["bedrooms"],
        h["dimensions"],
        h["price"],
        h["url"]
    ))

    conn.commit()
    conn.close()


def save_houses(houses: list):

    for house in houses:
        insert_house(house)

    print(f"💾 Saved {len(houses)} houses to PostgreSQL")