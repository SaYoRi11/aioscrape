import asyncio
from aiohttp import ClientSession
from urls import urls
from bs4 import BeautifulSoup
from pprint import pprint

async def get_html(url, session):
    resp = await session.request(method="GET", url=url)
    resp.raise_for_status()
    html = await resp.text()
    return html

# Get internal links from a url
async def scrape(url, session):
    try:
        html = await get_html(url, session)
    except Exception as e:
        print(e)
    else:
        soup = BeautifulSoup(html, 'lxml')
        links = [link['href'] for link in soup.find_all('a', href = True) if link['href'].startswith('/')]
        return links


async def start():
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(scrape(url, session))
            task.idx = url
            tasks.append(task)
        done, _ = await asyncio.wait(tasks)
        results = {
            task.idx: task.result() for task in done
        }

        pprint(results)

if __name__ == '__main__':
    asyncio.run(start())