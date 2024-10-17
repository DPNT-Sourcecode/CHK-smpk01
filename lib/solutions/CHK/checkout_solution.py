

# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter

products = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def checkout(skus: str) -> int:
    prices = Counter(skus)

    if not set(prices).issubset(products):
        return -1
    
    cost = 0

    if 'E' in prices:
        prices['B'] = prices.get('B', 0) - prices['E']//2
        if prices['B'] <= 0:
            del prices['B']
        cost += prices['E'] * 40
    if 'A' in prices:
        cost += (prices['A']//5) * 200
        prices['A'] %= 5
        cost += (prices['A']//3) * 130
        prices['A'] %= 3
        cost += prices['A'] * 50
    if 'B' in prices:
        cost += (prices['B']//2) * 45
        prices['B'] %= 2
        cost += prices['B'] * 30
    if 'C' in prices:
        cost += prices['C'] * 20
    if 'D' in prices:
        cost += prices['D'] * 15
    if 'F' in prices:
        cost += (prices['F']//3) * 20
        cost += (prices['F']%3) * 10
    if 'G' in prices:
        cost += prices['G']*20
    if 'H' in prices:
        cost += (prices['H']//10) * 80
        prices['H'] %= 10
        cost += (prices['H']//5) * 45
        prices['H'] %= 5
        cost += prices['H'] * 10
    if 'I' in prices:
        cost += prices['I'] * 35
    if 'J' in prices:
        cost += prices['J'] * 60
    if 'K' in prices:
        cost += (prices['K']//2) * 150
        prices['K'] %= 2
        cost += prices['K'] * 80
    if 'L' in prices:
        cost += prices['L'] * 90
    if 'N' in prices:
        prices['M'] = prices.get('M', 0) - prices['N']//3
        if prices['M'] <= 0:
            del prices['M']
        cost += prices['N'] * 40
    if 'M' in prices:
        cost += prices['M'] * 15
    if 'O' in prices:
        cost += prices['O'] * 10
    if 'P' in prices:
        cost += (prices['P']//5) * 200
        prices['P'] %= 5
        cost += prices['P'] * 50
    if 'R' in prices:
        prices['Q'] = prices.get('Q', 0) - prices['R']//3
        if prices['Q'] <= 0:
            del prices['Q']
        cost += prices['R'] * 50
    if 'Q' in prices:
        cost += (prices['Q']//3) * 80
        prices['Q'] %= 3
        cost += prices['Q'] * 30
    if 'S' in prices:
        cost += prices['S'] * 30
    if 'T' in prices:
        cost += prices['T'] * 20
    if 'U' in prices:
        cost += (prices['U']//4) * 120
        prices['U'] %= 4
        cost += prices['U'] * 40
    if 'V' in prices:
        cost += (prices['V']//3) * 130
        prices['V'] %= 3
        cost += (prices['V']//2) * 90
        prices['V'] %= 2
        cost += prices['V'] * 50

    return cost