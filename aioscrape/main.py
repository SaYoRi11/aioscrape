import asyncio
import csv
from aiohttp import ClientSession

from aioscrape.urls import urls
from aioscrape.daraz import get_products
from aioscrape.utils import process

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

        products = []
        for url in results:
            products.extend(get_products(results[url]))
        
        with open('aioscrape/csv/products.csv', 'w+') as file:
            writer = csv.DictWriter(file, fieldnames=['name'])
            writer.writeheader()
            writer.writerows(products)

        process(input_file='aioscrape/csv/products.csv')

if __name__ == '__main__':
    asyncio.run(start())