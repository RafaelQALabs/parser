import aiohttp


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


async def fetch(session, url, params=None):
    async with session.get(url, params=params) as resp:
        return await resp.text()