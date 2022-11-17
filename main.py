import asyncio
from aiohttp import ClientSession
from urls import urls
from bs4 import BeautifulSoup
from pprint import pprint


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
                html = await resp.text()
                results[task.idx] = html

        pprint(exceptions)
        pprint(results)

if __name__ == '__main__':
    asyncio.run(start())