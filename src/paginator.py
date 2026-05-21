from bs4 import BeautifulSoup


def get_next_page(html: str):
    soup = BeautifulSoup(html, "lxml")

    next_btn = soup.select_one("a.next.page-numbers")

    if not next_btn:
        return None

    return next_btn.get("href")