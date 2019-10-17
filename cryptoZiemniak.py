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

    def get_occurances(self) -> dict:
        return self._dictionary

    def get_total(self) -> int:
        return self._total

    def get_probability(self) -> dict:
        probability = {}
        for key in self._dictionary:
            probability[key] = self._dictionary[key] / self._total
        return probability


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