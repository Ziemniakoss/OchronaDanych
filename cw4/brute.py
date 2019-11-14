import sys
import crypt
import string
import random
from cryptoZiemniak import passwordGenerator

password = crypt.crypt("haslo")
a = string.ascii_letters
lastChar = a[0]
i = 0
for p in passwordGenerator(5, a):
    i += 1
    if i % 1000 == 0:
        print(i)
    if lastChar != p[0]:
        print(p[0])
        lastChar = p[0]
    trial = crypt.crypt(p, password)
    if password == trial:
        print("Hasło to {}".format(p))
        break
