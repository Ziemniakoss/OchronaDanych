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


def extendedEuclidean(a: int, b: int) -> dict:
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return {"x": old_s,
            "y": old_t,
            "NWD": old_r}


def invModulo(n: int, mod: int):
    x = extendedEuclidean(n, mod)
    if x["NWD"] != 1:
        raise Exception("Nie ma")
    else:
        return x["x"] % mod
