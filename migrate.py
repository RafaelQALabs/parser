import sqlite3
import psycopg2

# SQLite
sqlite_conn = sqlite3.connect("data/houses.db")
sqlite_cursor = sqlite_conn.cursor()

# PostgreSQL
pg_conn = psycopg2.connect(
    dbname="postgres",
    user="rafagima",
    password="",
    host="localhost",
    port="5432"
)

pg_cursor = pg_conn.cursor()

# создаем таблицу
pg_cursor.execute("""
CREATE TABLE IF NOT EXISTS houses (
    id SERIAL PRIMARY KEY,
    title TEXT,
    total_area REAL,
    living_area REAL,
    floors INTEGER,
    bedrooms INTEGER,
    dimensions TEXT,
    price INTEGER,
    url TEXT
)
""")

# читаем sqlite
sqlite_cursor.execute("""
SELECT
    title,
    total_area,
    living_area,
    floors,
    bedrooms,
    dimensions,
    price,
    url
FROM houses
""")

rows = sqlite_cursor.fetchall()

# вставляем в postgres
for row in rows:
    pg_cursor.execute("""
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
    """, row)

pg_conn.commit()

print(f"Moved {len(rows)} rows")

sqlite_conn.close()
pg_conn.close()