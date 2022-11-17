import asyncio
from aiohttp import ClientSession
from aioscrape.urls import urls
from pprint import pprint
from aioscrape.daraz import get_products


async def scrape(url, session):
    resp = await session.request(method="GET", url=url)
    resp.raise_for_status()
    return resp


async def start():
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(scrape(url, session))
            task.idx = url
            tasks.append(task)

        done, _ = await asyncio.wait(tasks)
        results = {}
        exceptions = {}
        for task in done:
            exc = task.exception()
            if exc:
                exceptions[task.idx] = exc
            else:
                resp = task.result()
                data = await resp.json()
                results[task.idx] = data

        products = {
            url: get_products(results[url]) for url in results
        }
        pprint(products)

if __name__ == '__main__':
    asyncio.run(start())