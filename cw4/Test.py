# from hashlib import md5
# import sys, string, crypt
# import os, errno
# import htpasswd
# from typing import Tuple, List, Iterable
# from Crypto.Cipher import ARC4
# from itertools import product, takewhile
# from IPython.display import clear_output
# import passlib.hash

import sys
import crypt
import string
import random

import hashlib
import cryptoZiemniak as cz

# systemowa crypt
print("WYkorzystanie systemowiej funkcji crypt")
print("Password: ", end="")
password = input()
salt = cz.randomString(2)

protectedPassword = crypt.crypt(password, salt)
print(salt)
print(protectedPassword)

args = sys.argv

print("Hashowanie sha256,\n password:", end="")
password = input().encode("utf-8")
h = hashlib.sha3_256(password)
print(h)
print(h.digest())
print(h.hexdigest())

chc = string.ascii_letters
i = 0
for password in cz.passwordGenerator(10, chc):
    i += 1
    if i % 500 == 0:
        print(i)
    # print(password)

print(i)
