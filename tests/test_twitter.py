import asyncio
import os
from aiohttp import ClientSession

from aioscrape.twitter.scrape import scrape_bio
from aioscrape.twitter.token import get_guest_token


def test_bio_scraper():
    profiles = ['elonmusk', 'MarcusRashford',  'sajdkakdkakska', 'POTUS', 'KSI', 'FabrizioRomano', 'invalid profile']
    bios = asyncio.run(scrape_bio(profiles))
    assert bios['elonmusk'] == ''
    assert bios['MarcusRashford'] == 'Manchester United & England International Footballer ⚽️ Info@dnmaysportsmgt.com 📩'
    assert bios['sajdkakdkakska'] == None
    assert bios['POTUS'] == '46th President of the United States, husband to @FLOTUS, proud dad & pop. Tweets may be archived: https://t.co/HDhBZBkKpU\nText me: (302) 404-0880'
    assert bios['KSI'] == 'Founder of @PrimeHydrate CEO of @misfitsboxing // “Summer Is Over” out now https://t.co/vLtm8ZGH0K'
    assert bios['FabrizioRomano'] == 'Here we go! ©'
    assert bios['invalid profile'] == None


async def test_token():
    gt_path = 'aioscrape/twitter/gt'
    authorization_token = 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'

    if os.path.exists(gt_path):
        os.remove(gt_path)

    async with ClientSession() as session:
        gt_1 = await get_guest_token(session, authorization_token)
        assert os.path.exists(gt_path)
        with open(gt_path) as f:
            assert gt_1 == f.read()

        gt_2 = await get_guest_token(session, authorization_token)
        assert gt_1 == gt_2

        gt_3 = await get_guest_token(session, authorization_token, new=True)
        assert gt_1 != gt_3

    # Simulate expired token with invalid token
    with open(gt_path, 'w+') as f:
        f.write('621763727424')   

    # When we get error, new token is generated
    bios = await scrape_bio(['FabrizioRomano'])
    assert bios['FabrizioRomano'] == 'Here we go! ©'

    with open(gt_path) as f:
        assert f.read() != '621763727424'
 
if __name__ == '__main__':
    test_bio_scraper()
    asyncio.run(test_token())