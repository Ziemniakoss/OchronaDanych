from Crypto.Cipher import DES, AES
from Crypto.Random import get_random_bytes
from typing import Iterable
from Crypto.Protocol.KDF import PBKDF2
from itertools import product
from PIL import Image
import math
import hashlib
import os
from cryptoZiemniak import OccurrenceCalculator

def fileEntropy(fileName: str):
    file = open(fileName, "rb")
    occurances = {}
    total = 0
    for b in file.read():
        if b in occurances:
            occurances[b] += 1
        else:
            occurances[b] = 1
        total += 1
    prob = {}
    for key in occurances:
        prob[key] = occurances[key] / total

    entr = 0
    for key in prob:
        p = prob[key]
        if p != 0:
            entr += p * math.log(p)
    file.close()
    return -entr

print("Nazwa pliku: ", end="")
fileName = input()
print("Hasło: ", end="")
password = input()

print("Kodowanie")
inputFile = open(fileName, "rb")
outputFile = open(fileName+".aes", "wb")

key = PBKDF2(password, b'salt')

iv = get_random_bytes(16)
aes = AES.new(key, AES.MODE_CBC, iv)
while True:
    c = inputFile.read(16)
    if not c:
        break
    if len(c) != 16:
        a = bytes([ord('@')] * (16 - len(c)))
        c += a
    outputFile.write(aes.encrypt(c))
outputFile.flush()
outputFile.close()
inputFile.close()


print("Obliczanie entropii...")
print("Przed zakodowaniem: {}".format(fileEntropy(fileName)))
print("Po zakodowaniu:     {}".format(fileEntropy(fileName+".aes")))
