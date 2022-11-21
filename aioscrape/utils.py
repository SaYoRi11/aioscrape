import csv
import re
from aioscrape.units import units, normalize

QUANTITY_REGEX = r'(\d[\d,]*\.?\d*) ?(\w+)'
           

def parse_quantities(text):
    matches = re.findall(QUANTITY_REGEX, text)
    quantities = []
    for match in matches:
        if match[1].lower() in units:
            amount = float(match[0].strip().replace(',', ''))
            unit = units[match[1].lower()]
            if unit in normalize:
                amount = amount * normalize[unit]['factor']
                unit = normalize[unit]['convert_to']
            quantities.append((amount, unit))       
    return quantities


def write_to_csv(file, data, fieldnames):
    with open(file, 'w+') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


async def request(url, session, method="GET", headers={}):
    resp = await session.request(method=method, url=url, headers=headers)
    resp.raise_for_status()
    return resp
