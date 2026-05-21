# EcoCity Parser

Асинхронный парсер проектов домов с сайта EcoCity.

Парсер:

- работает через AJAX (`admin-ajax.php`)
- собирает все страницы каталога
- автоматически обходит пагинацию
- сохраняет данные в Excel
- использует `aiohttp` + `asyncio`

---

# Структура проекта

```bash
eco_parser/
│
├── data/
│   └── output.xlsx
│
├── client_async.py
├── filters_async.py
├── main_async.py
├── parser.py
├── saver.py
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
python main_async.py
```

---

# Что делает парсер

Парсер:

1. Отправляет POST запросы на:

```txt
https://eco-city.spb.ru/wp-admin/admin-ajax.php
```

2. Получает HTML карточек домов

3. Парсит:

- название
- площадь
- этажность
- спальни
- размеры
- цену
- ссылку

4. Проверяет пагинацию

5. Переходит на следующую страницу

6. Сохраняет результат в:

```txt
data/output.xlsx
```

---

# Используемые технологии

- Python 3
- asyncio
- aiohttp
- BeautifulSoup4
- pandas
- openpyxl

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

## Сохранение Excel

Файл автоматически сохраняется в папку:

```txt
data/
```

Если папки нет — она создается автоматически.

---

# Возможные улучшения

Можно добавить:

- CSV export
- SQLite/PostgreSQL
- Proxy support
- Retry logic
- Logging
- Docker
- CLI arguments
- Unit tests
- Scrapy version

---
