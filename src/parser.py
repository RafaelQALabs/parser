from bs4 import BeautifulSoup


def parse_cards(html: str):
    soup = BeautifulSoup(html, "lxml")

    cards = soup.select("article.project")

    results = []

    for c in cards:
        title = c.select_one(".project__title")
        price = c.select_one(".project__price span")
        area = c.select(".project__area span")
        link = c.select_one("a.project__link")

        results.append({
            "title": title.get_text(strip=True) if title else None,
            "price": price.get_text(strip=True) if price else None,
            "area_total": area[0].get_text(strip=True) if len(area) > 0 else None,
            "area_living": area[1].get_text(strip=True) if len(area) > 1 else None,
            "url": link["href"] if link else None
        })

    return results