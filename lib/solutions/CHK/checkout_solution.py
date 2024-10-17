

# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter

def checkout(skus: str) -> int:
    prices = Counter(skus)

    if not set(prices).issubset(('A', 'B', 'C', 'D', 'E')):
        return -1
    
    cost = 0

    if 'E' in prices:
        free_Bs = prices['E']//2
        prices['B'] -= free_Bs
        cost += prices['E'] * 40
    if 'A' in prices:
        cost += (prices['A']//5) * 200
        prices['A'] %= 5
        cost += (prices['A']//3) * 130
        prices['A'] %= 3
        cost += prices['A'] * 50
    if 'B' in prices:
        cost += (prices['B']//2) * 45 + (prices['B']%2) * 30
    if 'C' in prices:
        cost += prices['C'] * 20
    if 'D' in prices:
        cost += prices['D'] * 15

    return cost



