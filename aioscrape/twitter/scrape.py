import asyncio
from aiohttp import ClientSession

from aioscrape.utils import request
from aioscrape.twitter.token import get_guest_token

authorization_token = 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'

async def scrape(session, profiles, gt):
    headers = {
        'authorization': authorization_token, 
        'x-guest-token': gt
     }

    tasks = []
    for profile in profiles:
        url = f'https://twitter.com/i/api/graphql/ptQPCD7NrFS_TW71Lq07nw/UserByScreenName?variables=%7B%22screen_name%22%3A%22{profile}%22%2C%22withSafetyModeUserFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Atrue%7D&features=%7B%22responsive_web_twitter_blue_verified_badge_is_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%7D'
        task = asyncio.create_task(request(url, session, headers=headers))
        task.idx = profile
        tasks.append(task)

    done, _ = await asyncio.wait(tasks)
    exceptions = {}
    results = {}
    for task in done:
        exc = task.exception()
        if exc:
            if exc.status == 403:   
                return None
            exceptions[task.idx] = exc
            results[task.idx] = None
        else:
            resp = task.result()
            json = await resp.json()
            try:
                results[task.idx] = json['data']['user']['result']['legacy']['description']
            except KeyError:   # When profile does not exist 
                results[task.idx] = None
    
    return results


async def scrape_bio(profiles):
    if not profiles:
        return {}

    async with ClientSession() as session:
        gt = await get_guest_token(session, authorization_token)
        bios = await scrape(session, profiles, gt)   
        if not bios:
            gt = await get_guest_token(session, authorization_token, new=True)
            bios = await scrape(session, profiles, gt)
        return bios


if __name__ == '__main__':
    asyncio.run(scrape_bio(['Cristiano']))