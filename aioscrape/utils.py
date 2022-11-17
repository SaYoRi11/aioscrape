import csv
import re

QUANTITY_REGEX = r'(\d[\d,X ]*\.?\d*)(\w+)'

units = ("gm", "gram", "g", "grams", "gms",
        "k", "kg", "kilo", "kilogram", "kilograms", "kgs",
        "pcs", "pieces", 'pc', 'piece',
         "l", "ml", "litres", "litre", "millilitres", "millilitre"
    )

def process(input_file, output_file='aioscrape/csv/quantities.csv'):
    with open(input_file) as file:
        reader = csv.reader(file)
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
            
    
    with open(output_file, 'w+') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'amount', 'unit'])
        writer.writeheader()
        writer.writerows(new_rows)


def parse_quantities(text):
    matches = re.findall(QUANTITY_REGEX, text)
    return [(match[0].strip(), match[1].strip()) for match in matches if match[1].lower() in units]


if __name__ == '__main__':
    process(input_file='aioscrape/csv/products.csv')