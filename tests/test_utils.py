from aioscrape.utils import parse_quantities

def test_quantities():
    texts = [
        'JUAS Quinoa (Pre-washed) - 1.5kg',
        'Wai Wai Dynamite Extra Spicy Instant Noodles (5 X 100gm pack) [Free Stainless Steel Bowl 2 pc]',
        'Big Choice Rajma Nepali -10g',
        'Wai Wai Chicken 65 Gm (Pack of 30 noodles)',
        'Tofu 400 gm 1Pcs',
        'Pokka Ice Lemon Tea 500ml'
    ]

    quantities = [parse_quantities(text) for text in texts]
    assert quantities[0] == [('1.5', 'kg')]
    assert quantities[1] == [('5 X 100', 'gm'), ('2', 'pc')]
    assert quantities[2] == [('10', 'g')]
    assert quantities[3] == [('65', 'Gm')]
    assert quantities[4] == [('400', 'gm'), ('1', 'Pcs')]
    assert quantities[5] == [('500', 'ml')]

if __name__ == '__main__':
    test_quantities()