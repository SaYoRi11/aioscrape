from aioscrape.utils import parse_quantities

def test_quantities():
    texts = [
        'JUAS Quinoa (Pre-washed) - 1.5kg',
        'Wai Wai Dynamite Extra Spicy Instant Noodles (5 X 100gm pack) [Free Stainless Steel Bowl 2 pc]',
        'Big Choice Rajma Nepali -10g',
        'Wai Wai Chicken 65 Gm (Pack of 30 noodles)',
        'Tofu 400 gm 1Pcs',
        'Pokka Ice Lemon Tea 500ml',
        '7.5 litres of tea',
        '1,100 mgs of msg'
    ]

    quantities = [parse_quantities(text) for text in texts]
    assert quantities[0] == [(1500, 'g')]
    assert quantities[1] == [(100, 'g'), (2, 'pcs')]
    assert quantities[2] == [(10, 'g')]
    assert quantities[3] == [(65, 'g')]
    assert quantities[4] == [(400, 'g'), (1, 'pcs')]
    assert quantities[5] == [(500, 'ml')]
    assert quantities[6] == [(7500, 'ml')]
    assert quantities[7] == [(1.1, 'g')]

if __name__ == '__main__':
    test_quantities()