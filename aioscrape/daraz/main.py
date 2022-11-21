import asyncio
import csv
import os
from aiohttp import ClientSession

from aioscrape.daraz.scrape import get_products
from aioscrape.utils import parse_quantities, request, write_to_csv


async def scrape(url, session, products_file):
    print('Scraping...')
    task = asyncio.create_task(request(url, session))
    task.idx = url

    done, _ = await asyncio.wait([task])
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

    products = get_products(results[url])
    if not products:
        print('Nothing found!')
        return
    write_to_csv(products_file, products, fieldnames=['name'])


def process(input_file, output_file):
    if not os.path.exists(input_file):
        return
    with open(input_file) as file:
        reader = csv.reader(file)
        print('Processing...')
        # Skip the header row
        next(reader, None)
        new_rows = []
        for row in reader:
            quantities = parse_quantities(row[0])
            if not quantities:
                new_rows.append({
                    'name': row[0],
                    'amount': None,
                    'unit': None
                })
            else:
                for q in quantities:
                    new_rows.append({
                        'name': row[0],
                        'amount': q[0],
                        'unit': q[1]
                    })
    write_to_csv(output_file, new_rows, fieldnames=['name', 'amount', 'unit']) 


async def start(term):
    if not term:
        return
        
    url = f'https://www.daraz.com.np/catalog/?q={term}&ajax=true'
    products_file = f'aioscrape/csv/raw/{term}.csv'

    if not os.path.exists(products_file):
        async with ClientSession() as session:
            await scrape(url, session, products_file)    

    output_file = f'aioscrape/csv/processed/{term}_quantities.csv'
    process(input_file=products_file, output_file=output_file)


if __name__ == '__main__':
    asyncio.run(start('rice'))