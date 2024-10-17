

# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter

def checkout(skus: str) -> int:
    prices = Counter(skus)

    if not set(prices).issubset(('A', 'B', 'C', 'D')):
        return -1
    
    cost = 0

    if 'A' in prices:
        cost += (prices['A']//3) * 130 + (prices['A']%3) * 50
    if 'B' in prices:
        cost += (prices['B']//2) * 45 + (prices['B']%2) * 30
    if 'C' in prices:
        cost += prices['C'] * 20
    if 'D' in prices:
        cost += prices['D'] * 15

    return cost

