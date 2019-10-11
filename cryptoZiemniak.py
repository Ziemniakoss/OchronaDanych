import math


class OccurrenceCalculator:
    def __init__(self, values: list):
        self._dictionary = {}
        for i in values:
            self._dictionary[i] = 0
        self._total = 0

    def add(self, value):
        if value in self._dictionary:
            self._dictionary[value] += 1
            self._total += 1

    def get_dictionary(self) -> dict:
        return self._dictionary

    def get_total(self) -> int:
        return self._total

    def probability_dic(self) -> dict:
        probability = {}
        for key in self._dictionary:
            probability[key] = self._dictionary[key] / self._total
        return probability

    def __str__(self) -> str:
        result = ""
        for key in self._dictionary:
            result += "{} <=> {}\n".format(key, self._dictionary[key])
        return result


class Cesar:
    def __init__(self, start: int, end: int, shift: int):
        if start >= end:
            raise ValueError("Invalid range")
        self._end = end
        self._start = start
        self._delta = self._end - self._start + 1
        self._shift = shift

    def encrypt(self, message: str) -> str:
        encrypted = ""
        for char in message:
            code = ord(char) - self._start
            if 0 <= code <= self._delta:
                code = (code + self._shift) % self._delta
                code += self._start

                encrypted += chr(code)
            else:
                ValueError("Char out of bounds: " + chr(code + self._start))
        return encrypted

    def decrypt(self, message: str) -> str:
        decrypted = ""
        for char in message:
            code = ord(char) - self._start
            if 0 <= code <= self._delta:
                code = ((code - self._shift) % self._delta) + self._start
                decrypted += chr(code)
            else:
                ValueError("Char out of bounds: " + chr(code + self._start))
        return decrypted


class Vigenere:
    def __init__(self, start: int, end: int, key: str):
        if start >= end:
            raise ValueError("Illegal range")
        self._start = start
        self._end = end
        self._delta = end - start + 1
        self._key = key

    def encrypt(self, message: str) -> str:
        encrypted = ""
        keyLen = len(self._key)
        for i in range(0, len(message)):
            code1 = ord(message[i]) - self._start
            code2 = ord(self._key[i % keyLen]) - self._start
            code = ((code1 + code2) % self._delta) + self._start
            encrypted += chr(code)
        return encrypted

    def decrypt(self, message: str) -> str:
        decrypted = ""
        keyLen = len(self._key)
        for i in range(0, len(message)):
            code1 = ord(self._key[i % keyLen]) - self._start
            code2 = ord(message[i]) - self._start
            code = ((code2 - code1) % self._delta) + self._start
            decrypted += chr(code)
        return decrypted


class RC4:
    def __init__(self, key: str):
        self._key = key

    def _generate_key(self):
        s = [i for i in range(256)]
        j = 0
        for i in range(256):
            j = (j + s[i] + ord(self._key[i % len(self._key)])) % 256
            s[i], s[j] = s[j], s[i]
        return s

    def encrypt(self, message: str) -> str:
        encrypted = ""
        s = self._generate_key()
        i, j = 0, 0

        for char in message:
            i = (i + 1) % 256
            j = (j + s[i]) % 256
            s[i], s[j] = s[j], s[i]
            k = s[(s[i] + s[j]) % 256]
            encrypted += chr(ord(char) ^ k)
        return encrypted


def entropy(data: bytes) -> float:
    # calc = OccurrenceCalculator([i for i in range(256)])
    # for x in data:
    #     calc.add(x)
    # prob = calc.probability_dic()
    # sum = 0
    # for key in prob:
    #     print(prob[key])
    #     sum += prob[key] * prob[key]
    # return 1 - sum / calc.get_total()
    count = [0] * 256
    dataSize = len(data)
    for b in data: count[b] = count[b] + 1

    entropy = 0
    for b in range(256):
        entropy += (count[b] / dataSize) * count[b]

    return 1 - entropy / dataSize
