""" 네이버 코믹스 조회 API"""
import asyncio

import aiohttp


async def fetch_naver_comic():
    """네이버 코믹스 조회 API 인기순"""
    url = "https://comic.naver.com/api/webtoon/titlelist/weekday?week=mon&order=user"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36",  # 여기에 사용자 에이전트 정보를 입력하세요.
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            # HTTP 응답 코드를 확인합니다.
            if response.status != 200:
                print(f"Error: {response.status}")
                return None

            # JSON 형식으로 응답을 읽습니다.
            data = await response.json()
            return data


async def main():
    """비동기로 실행"""
    naver_comic_data = await fetch_naver_comic()

    if naver_comic_data:
        # 여기에서 데이터를 활용하여 원하는 작업을 수행합니다.
        print(naver_comic_data)
        print(naver_comic_data["titleList"][4]["titleName"])
    else:
        print("Failed to fetch data.")


# 이벤트 루프를 실행합니다.
if __name__ == "__main__":
    asyncio.run(main())
