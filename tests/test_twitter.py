import asyncio
from aioscrape.twitter.scrape import scrape_bio

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

if __name__ == '__main__':
    test_bio_scraper()