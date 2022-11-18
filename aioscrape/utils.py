import csv
import re
from aioscrape.units import units

QUANTITY_REGEX = r'(\d[\d,X ]*\.?\d*)(\w+)'
           

def parse_quantities(text):
    matches = re.findall(QUANTITY_REGEX, text)
    quantities = []
    for match in matches:
        if match[1].lower() in units:
            quantities.append((match[0].strip(), units[match[1].lower()]))       
    return quantities


def write_to_csv(file, data, fieldnames):
    with open(file, 'w+') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


async def request(url, session):
    resp = await session.request(method="GET", url=url)
    resp.raise_for_status()
    return resp
