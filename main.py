from math import factorial
from collections import Counter

def decomp(n):
    n = factorial(n)
    d = 2
    factors = []

    while d**2 <= n:
        if n%d == 0:
            factors.append(d)
            n //= d
        else:
            d += 1

    if n > 1:
        factors.append(n)

    counter = Counter(factors)
    dec = [f'{k}^{v}' if v != 1 else f'{k}' for k, v in counter.items()]
    return " * ".join(dec)

