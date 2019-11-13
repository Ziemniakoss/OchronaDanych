import math


def sieve(limit: int) -> list:
    p = 2
    d = {i: True for i in range(2, limit, 1)}  # val -> is prime?
    while p < limit:
        for i in range(2 * p, limit, p):
            d[i] = False
        found: bool = False
        for i in range(p + 1, limit, 1):
            if d[i]:
                found = True
                p = i
                break
        if not found:
            break
    primes = []
    for i in d:
        if d[i]:
            primes.append(i)
    return primes


def findNextPrime(x: int):
    while True:
        x += 1
        found = True
        for i in range(2, math.floor(math.sqrt(x)) + 1, 1):
            if x % i == 0:
                found = False
                break
        if found:
            return x


def nwd(a: int, b: int) -> int:
    while b != 0:
        c = a % b
        a, b = b, c
    return a


def areSemiPrime(a: int, b: int) -> bool:
    return nwd(a, b) == 1


text = "ala ma kota"
print(type(text.encode()))
print(nwd(1, 1))
print(nwd(2, 1))
print(nwd(2, 4))
print(nwd(4, 8))
print(nwd(8, 4))
print(nwd(282, 78))
print(nwd(78, 282))
