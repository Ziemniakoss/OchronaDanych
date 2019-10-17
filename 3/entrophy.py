import math

a = "abcdefghijklmnopqrstuvwxyz"
filename = "../shakespear.txt"


class OccurrenceCalculator:
    def __init__(self, alphabet: str):
        self._occur = {}
        for char in alphabet:
            self._occur[char] = 0
        self._total = 0

    def add(self, string: str):
        string = string.lower()
        for char in string:
            if char in self._occur:
                self._occur[char] += 1
                self._total += 1

    def get_prob(self) -> dict:
        prob = {}
        for char in self._occur:
            prob[char] = self._occur[char] / self._total
        return prob

    def get_occur(self) -> dict:
        return self._occur


def entrophy(prob: dict):
    e = 0
    for char in prob:
        e += prob[char] * math.log2(prob[char])
    return -e


oc = OccurrenceCalculator(a)
file = open(filename)
while True:
    c = file.read(1)
    if not c:
        break
    oc.add(c)

prob = oc.get_prob()
print(entrophy(prob))
