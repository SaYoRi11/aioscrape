import csv
import re

QUANTITY_REGEX = r'(\d[\d,X ]*\.?\d*)(\w+)'

units = ("gm", "gram", "g", "grams", "gms",
        "k", "kg", "kilo", "kilogram", "kilograms", "kgs",
        "pcs", "pieces", 'pc', 'piece',
         "l", "ml", "litres", "litre", "millilitres", "millilitre"
    )       
    

def parse_quantities(text):
    matches = re.findall(QUANTITY_REGEX, text)
    return [(match[0].strip(), match[1].strip()) for match in matches if match[1].lower() in units]


def write_to_csv(file, data, fieldnames):
    with open(file, 'w+') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


async def request(url, session):
    resp = await session.request(method="GET", url=url)
    resp.raise_for_status()
    return resp
