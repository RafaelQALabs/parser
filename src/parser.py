from bs4 import BeautifulSoup


def parse_cards(html: str):

    soup = BeautifulSoup(html, "lxml")
    cards = soup.select("article.project")

    results = []

    for i, c in enumerate(cards):

        title = c.select_one(".project__title")
        price = c.select_one(".project__price span")
        areas = c.select(".project__area span")
        chars = c.select("p.project__char span")
        link = c.select_one("a.project__link")

        # защита от кривого HTML
        def get(lst, idx):
            return lst[idx].get_text(strip=True) if len(lst) > idx else None

        total_area = get(areas, 0)
        living_area = get(areas, 1)

        floors = get(chars, 2)
        bedrooms = get(chars, 3)
        dimensions = get(chars, 4)

        item = {
            "title": title.get_text(strip=True) if title else None,
            "total_area": total_area,
            "living_area": living_area,
            "floors": floors,
            "bedrooms": bedrooms,
            "dimensions": dimensions,
            "price": price.get_text(strip=True) if price else None,
            "url": link["href"] if link else None
        }

        # # 🔥 DEBUG (важно оставить)
        # print(f"\nCARD {i}")
        # print(item)

        results.append(item)

    return results