# EcoCity Scraper

Асинхронный парсер проектов домов с сайта EcoCity.

Проект собирает данные каталога домов через AJAX API, автоматически обходит пагинацию, сохраняет данные в PostgreSQL и экспортирует результат в Excel.

---

# Features

- Async scraping via `aiohttp`
- Pagination support
- AJAX requests (`admin-ajax.php`)
- PostgreSQL integration
- Docker support
- Excel export (`.xlsx`)
- Data normalization
- Duplicate protection (`ON CONFLICT DO NOTHING`)
- Modular architecture

---

# Tech Stack

- Python 3.12
- asyncio
- aiohttp
- BeautifulSoup4
- pandas
- openpyxl
- PostgreSQL
- psycopg2
- Docker
- Docker Compose

---

# Project Structure

```bash
eco-city-scraper/
│
├── data/
│   └── output.xlsx
│
├── src/
│   ├── client.py
│   ├── parser.py
│   ├── paginator.py
│   ├── exporter.py
│   ├── database.py
│   ├── scraper.py
│   └── filters.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── migrate.py
├── .gitignore
└── README.md
```

---

# Installation

## Clone repository

```bash
git clone <repo_url>
cd eco-city-scraper
```

---

# Run with Docker

## Start containers

```bash
docker compose up -d --build
```

## View logs

```bash
docker compose logs -f
```

---

# PostgreSQL

The project uses PostgreSQL inside Docker.

Database config:

| Variable | Value |
|---|---|
| DB Name | scraper_db |
| User | admin |
| Port | 5432 |

---

# Database Schema

Table: `houses`

| Column | Type |
|---|---|
| id | SERIAL |
| title | TEXT |
| total_area | REAL |
| living_area | REAL |
| floors | INTEGER |
| bedrooms | INTEGER |
| dimensions | TEXT |
| price | INTEGER |
| url | TEXT UNIQUE |

---

# SQL Schema

```sql
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
);
```

---

# Example SQL Queries

## Get all houses

```sql
SELECT * FROM houses;
```

## Houses cheaper than 2M

```sql
SELECT * FROM houses
WHERE price < 2000000;
```

## One-floor houses

```sql
SELECT * FROM houses
WHERE floors = 1;
```

## Houses with 3 bedrooms

```sql
SELECT * FROM houses
WHERE bedrooms = 3;
```

---

# What the scraper does

The scraper:

1. Sends AJAX requests to:

```text
https://eco-city.spb.ru/wp-admin/admin-ajax.php
```

2. Parses house cards

3. Extracts:

- title
- total area
- living area
- floors
- bedrooms
- dimensions
- price
- url

4. Detects pagination

5. Saves data into:

- PostgreSQL
- Excel (`data/output.xlsx`)

---

# Output

After execution:

- PostgreSQL table is populated
- Excel file is generated

Example:

```bash
DONE: 73
Saved 73 houses to PostgreSQL
Saved to data/output.xlsx
```

---

# Run Without Docker

## Create virtual environment

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run scraper

```bash
python src/scraper.py
```

---

# Future Improvements

Possible improvements:

- FastAPI REST API
- SQLAlchemy ORM
- Alembic migrations
- Retry logic
- Logging
- Proxy rotation
- CLI arguments
- Unit tests
- CI/CD
- Web dashboard
- Telegram notifications

---

# Architecture

```text
EcoCity Website
        ↓
 AJAX Requests
        ↓
 Async Scraper
        ↓
 Data Parser
        ↓
 PostgreSQL
        ↓
 Excel Export
```

---

# Author

Rafael Gima