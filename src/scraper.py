import asyncio
import aiohttp

from client import fetch, HEADERS
from parser import parse_cards
from paginator import get_next_page
from exporter import save_to_excel
from database import create_table, save_houses

BASE_URL = "https://eco-city.spb.ru/products"


async def run():
    print("🚀 Starting scraper")

    create_table()
    all_data = []
    visited = set()

    async with aiohttp.ClientSession(headers=HEADERS) as session:

        url = BASE_URL

        while url:

            if url in visited:
                print("🛑 loop detected")
                break

            visited.add(url)

            print(f"📄 {url}")

            html = await fetch(session, url)

            items = parse_cards(html)

            print(f"✔ items: {len(items)}")

            all_data.extend(items)

            next_url = get_next_page(html)   # 🔥 FIX HERE

            if not next_url:
                print("🛑 no next page")
                break

            url = next_url

    print("\nDONE:", len(all_data))

    save_houses(all_data)
    save_to_excel(all_data)


if __name__ == "__main__":
    asyncio.run(run())