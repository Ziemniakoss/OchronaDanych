from cw6.primes import areSemiPrime, invModulo
from random import randint
from cw6.utils6 import textToCodeBlocks


class Key:
    def __init__(self, exp: int, mod: int):
        self._exp = exp
        self._mod = mod

    def getMod(self):
        return self._mod

    def getExp(self):
        return self._exp

    def __str__(self):
        return f'exp={self._exp}, mod={self._mod}'


class RSA:
    def __init__(self, p: int, q: int):
        n = p * q
        euler = (p - 1) * (q - 1)
        # wybieramy e
        while True:
            e = randint(1, euler)
            if areSemiPrime(e, euler):
                break
        d = invModulo(e, euler)
        self._e = e
        self._d = d
        self._n = n
        self._private = Key(e, n)
        self._public = Key(d, n)

    def encrypt(self, message: str):
        key = self.public()
        blocks = textToCodeBlocks(message, 2, 0)
        for block in blocks:
            for i in range(len(block)):
                block[i] = pow(block[i], key.getExp(), key.getMod())
        return blocks

    def decrypt(self, blocks: list):
        key = self.private()
        result = ""
        for block in blocks:
            for code in block:
                result += chr(pow(code, key.getExp(), key.getMod()))
        return result

    def public(self):
        return self._public

    def private(self):
        return self._private


pow(2, 3)
message = "ale ma kota a kot ma ale" * 20
rsa = RSA(409, 1747)

encoded = rsa.encrypt(message)
print(encoded)
decoded = rsa.decrypt(encoded)
print(decoded)
