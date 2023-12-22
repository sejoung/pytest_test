""" 네이버 코믹스 조회 API"""

import aiohttp


async def fetch_naver_comic():
    """네이버 코믹스 조회 API 인기순"""
    url = "https://comic.naver.com/api/webtoon/titlelist/weekday?week=mon&order=user"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36",
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status != 200:
                print(f"Error: {response.status}")
                return None

            # JSON 형식으로 응답을 읽습니다.
            data = await response.json()
            return data
