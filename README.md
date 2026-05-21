# EcoCity Parser

Асинхронный парсер проектов домов с сайта EcoCity.

Парсер:

- работает через AJAX (`admin-ajax.php`)
- собирает все страницы каталога
- автоматически обходит пагинацию
- сохраняет данные в Excel
- сохраняет данные в SQLite
- использует `aiohttp` + `asyncio`

---

# Структура проекта

```bash
eco_parser/
│
├── data/
│   ├── output.xlsx
│   └── houses.db
│
├── client.py
├── parser.py
├── paginator.py
├── exporter.py
├── database.py
├── scraper.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Установка

## 1. Клонировать проект

```bash
git clone <repo_url>
cd eco_parser
```

---

## 2. Создать виртуальное окружение

### Linux / macOS

```bash
python3 -m venv venv
```

### Windows

```bash
python -m venv venv
```

---

## 3. Активировать окружение

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows CMD

```cmd
venv\Scripts\activate
```

### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

---

## 4. Установить зависимости

```bash
pip install -r requirements.txt
```

---

# requirements.txt

```txt
aiohttp
beautifulsoup4
pandas
openpyxl
lxml
```

---

# Запуск

```bash
python scraper.py
```

---

# Что делает парсер

Парсер:

1. Отправляет AJAX запросы

```txt
https://eco-city.spb.ru/wp-admin/admin-ajax.php
```

2. Получает HTML карточек домов

3. Парсит:

- название
- общую площадь
- жилую площадь
- этажность
- количество спален
- размеры
- цену
- ссылку

4. Проверяет пагинацию

5. Переходит на следующую страницу

6. Сохраняет результат в:

```txt
data/output.xlsx
```

и:

```txt
data/houses.db
```

---

# SQLite Database

Парсер автоматически создает SQLite базу данных.

Файл базы:

```txt
data/houses.db
```

---

## Структура таблицы

Таблица:

```sql
houses
```

Поля:

| Поле | Тип |
|---|---|
| id | INTEGER |
| title | TEXT |
| total_area | REAL |
| living_area | REAL |
| floors | INTEGER |
| bedrooms | INTEGER |
| dimensions | TEXT |
| price | INTEGER |
| url | TEXT |

---

## SQL схема

```sql
CREATE TABLE IF NOT EXISTS houses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
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

## Примеры SQL запросов

### Получить все дома

```sql
SELECT * FROM houses;
```

---

### Найти дома дешевле 2 млн

```sql
SELECT * FROM houses
WHERE price < 2000000;
```

---

### Найти одноэтажные дома

```sql
SELECT * FROM houses
WHERE floors = 1;
```

---

### Найти дома с 3 спальнями

```sql
SELECT * FROM houses
WHERE bedrooms = 3;
```

---

# Просмотр SQLite базы

Базу можно открыть через:

- DB Browser for SQLite
- DBeaver
- DataGrip
- VSCode SQLite Extension

---

# Используемые технологии

- Python 3
- asyncio
- aiohttp
- BeautifulSoup4
- pandas
- openpyxl
- SQLite3

---

# Особенности

## Асинхронность

Используется:

```python
asyncio
aiohttp
```

Это позволяет быстрее загружать страницы.

---

## Пагинация

Парсер автоматически определяет:

```html
<a class="next page-numbers">
```

и продолжает сбор данных.

---

## Excel Export

Файл автоматически сохраняется в папку:

```txt
data/
```

Если папки нет — она создается автоматически.

---

## SQLite Integration

Данные одновременно сохраняются:

- в Excel
- в SQLite

Это позволяет выполнять SQL запросы и использовать данные в других проектах.

---

# Возможные улучшения

Можно добавить:

- CSV export
- PostgreSQL
- Docker
- FastAPI
- REST API
- Retry logic
- Logging
- Proxy support
- CLI arguments
- Unit tests
- Scrapy version
- Telegram Bot
- Web Dashboard

---
