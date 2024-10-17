

# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter

products = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def checkout(skus: str) -> int:
    prices = Counter(skus)

    if not set(prices).issubset(products):
        return -1
    
    cost = 0

    # always make sure to remove items if their count is 0

    if 'A' in prices:
        cost += (prices['A']//5) * 200
        prices['A'] %= 5
        cost += (prices['A']//3) * 130
        prices['A'] %= 3
        cost += prices['A'] * 50

        del prices['A']

    # E before B
    if 'E' in prices:
        prices['B'] = prices.get('B', 0) - prices['E']//2
        if prices['B'] <= 0:
            del prices['B']
        cost += prices['E'] * 40

        del prices['E']

    if 'B' in prices:
        cost += (prices['B']//2) * 45
        prices['B'] %= 2
        cost += prices['B'] * 30

        del prices['B']

    if 'C' in prices:
        cost += prices['C'] * 20

        del prices['C']

    if 'D' in prices:
        cost += prices['D'] * 15

        del prices['D']

    if 'F' in prices:
        cost += (prices['F']//3) * 20
        cost += (prices['F']%3) * 10

        del prices['F']

    if 'G' in prices:
        cost += prices['G'] * 20

        del prices['G']

    if 'H' in prices:
        cost += (prices['H']//10) * 80
        prices['H'] %= 10
        cost += (prices['H']//5) * 45
        prices['H'] %= 5
        cost += prices['H'] * 10

        del prices['H']

    if 'I' in prices:
        cost += prices['I'] * 35

        del prices['I']

    if 'J' in prices:
        cost += prices['J'] * 60

        del prices['J']

    if 'K' in prices:
        cost += (prices['K']//2) * 120
        prices['K'] %= 2
        cost += prices['K'] * 70

        del prices['K']

    if 'L' in prices:
        cost += prices['L'] * 90

        del prices['L']
        
    # N before M
    if 'N' in prices:
        prices['M'] = prices.get('M', 0) - prices['N']//3
        if prices['M'] <= 0:
            del prices['M']
        cost += prices['N'] * 40

        del prices['N']

    if 'M' in prices:
        cost += prices['M'] * 15

        del prices['M']

    if 'O' in prices:
        cost += prices['O'] * 10

        del prices['O']

    if 'P' in prices:
        cost += (prices['P']//5) * 200
        prices['P'] %= 5
        cost += prices['P'] * 50

        del prices['P']

    # R before Q
    if 'R' in prices:
        prices['Q'] = prices.get('Q', 0) - prices['R']//3
        if prices['Q'] <= 0:
            del prices['Q']
        cost += prices['R'] * 50

        del prices['R']

    if 'Q' in prices:
        cost += (prices['Q']//3) * 80
        prices['Q'] %= 3
        cost += prices['Q'] * 30

        del prices['Q']

    if 'U' in prices:
        cost += (prices['U']//4) * 120
        prices['U'] %= 4
        cost += prices['U'] * 40

        del prices['U']

    if 'V' in prices:
        cost += (prices['V']//3) * 130
        prices['V'] %= 3
        cost += (prices['V']//2) * 90
        prices['V'] %= 2
        cost += prices['V'] * 50

        del prices['V']

    if 'W' in prices:
        cost += prices['W'] * 20

        del prices['W']

    # group discount

    mapping_price = {
        'S': 20,
        'T': 20,
        'X': 17,
        'Y': 20,
        'Z': 21
    }

    while sum(prices.values()) >= 3:
        cost += 45
        for _ in range(3):
            biggest = max(prices, key=mapping_price.get)
            prices[biggest] -= 1
            if prices[biggest] == 0:
                del prices[biggest]
        
    if 'S' in prices:
        cost += prices['S'] * 20
    if 'T' in prices:
        cost += prices['T'] * 20
    if 'X' in prices:
        cost += prices['X'] * 17
    if 'Y' in prices:
        cost += prices['Y'] * 20
    if 'Z' in prices:
        cost += prices['Z'] * 21

    return cost


