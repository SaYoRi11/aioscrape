import os
import asyncio

from aioscrape.main import start

def test_start():
    asyncio.run(start('canned foods'))
    assert os.path.exists('aioscrape/csv/raw/canned foods.csv')
    assert os.path.exists('aioscrape/csv/processed/canned foods_quantities.csv')

    # Files not created if search term not found
    asyncio.run(start('dnajbdbaj'))
    assert not os.path.exists('aioscrape/csv/raw/dnajbdbaj.csv')
    
    asyncio.run(start(''))


if __name__ == '__main__':
    test_start()