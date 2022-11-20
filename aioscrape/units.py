units = {
    'mg': 'mg', 'milligram': 'mg', 'milligrams': 'mg', 'mgs': 'mg',
    'gm': 'g',  'gram': 'g', 'g': 'g', 'grams': 'g', 'gms': 'g', 
    'k': 'kg', 'kg': 'kg', 'kilo': 'kg', 'kilogram': 'kg', 'kilograms': 'kg', 'kgs': 'kg', 
    'pcs': 'pcs', 'pieces': 'pcs', 'pc': 'pcs', 'piece': 'pcs',
    'l': 'l', 'litres': 'l', 'litre': 'l', 'liter': 'l', 'liters': 'l', 
    'ml': 'ml', 'millilitres': 'ml', 'millilitre': 'ml', 'milliliter': 'ml', 'milliliters': 'ml'
}

normalize = {
    'kg': {
        'factor': 1000,
        'convert_to': 'g'
    },
    'mg': {
        'factor': 0.001,
        'convert_to': 'g'
    },
    'l': {
        'factor': 1000,
        'convert_to': 'ml'
    }
}