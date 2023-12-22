"""테스트 코드 작성"""
import pytest

import sample


@pytest.mark.asyncio
async def test_fetch_naver_comic():
    """네이버 코믹스 조회 API 테스트"""
    naver_comic_data = await sample.fetch_naver_comic()

    assert naver_comic_data
    assert naver_comic_data["titleList"][0]["titleName"] == "12시네점심"
