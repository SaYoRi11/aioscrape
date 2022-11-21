import os
import asyncio
import csv

from aioscrape.daraz.main import start

def test_start():
    input_path = 'aioscrape/csv/raw/canned foods.csv'
    output_path = 'aioscrape/csv/processed/canned foods_quantities.csv'
    if os.path.exists(input_path):
        os.remove(input_path)
    if os.path.exists(output_path):
        os.remove(output_path)
    
    asyncio.run(start('canned foods'))
    assert os.path.exists(input_path)
    assert os.path.exists(output_path)

    with open(input_path) as input_file:
        with open(output_path) as output_file:
            input_rows = csv.reader(input_file)
            output_rows = csv.reader(output_file)
            assert next(input_rows, None) == ['name']
            assert next(output_rows, None) == ['name', 'amount', 'unit']
            input = set([row[0] for row in input_rows])
            output = set([row[0] for row in output_rows])
            assert input == output            

    # Files not created if search term not found
    asyncio.run(start('dnajbdbaj'))
    assert not os.path.exists('aioscrape/csv/raw/dnajbdbaj.csv')
    
    asyncio.run(start(''))


if __name__ == '__main__':
    test_start()