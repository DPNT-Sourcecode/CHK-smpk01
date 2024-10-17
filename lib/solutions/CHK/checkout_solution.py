

# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter

def checkout(skus: str) -> int:
    prices = Counter(skus)

    if not set(prices).issubset(('A', 'B', 'C', 'D')):
        return -1
    
    return 0

