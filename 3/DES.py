import time
from Crypto.Cipher import DES, AES
from IPython.display import clear_output
from Crypto.Random import get_random_bytes

from Crypto.Protocol.KDF import PBKDF2

password = "Tajny klucz nie do zgadniecia"
message = "wiadnoso"
iv = get_random_bytes(8)
key = PBKDF2(password, b"salt")
key1 = key[0:8]

print("Kodujemy \"{}\" za pomocą DES i klucza \"{}\"".format(message, key1))

print("DES wykorzystujący CBC")
des = DES.new(key1, DES.MODE_CBC, iv)
des_chc = des.encrypt(message)
des = DES.new(key1, DES.MODE_CBC, iv)
print("\t", des.decrypt(des_chc), "->", des_chc)

print("Des wyjkorzystujacy ECB")
des = DES.new(key1, DES.MODE_ECB, iv)
des_ecb = des.encrypt(message)
des = DES.new(key1, DES.MODE_ECB, iv)
print("\t", des.decrypt(des_ecb), "->", des_ecb)
