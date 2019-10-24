from cryptoZiemniak import passwordGenerator
from Crypto.Protocol.KDF import PBKDF2
from PIL import Image
import math
from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES, AES
import string
import struct
import io
import cv2

fileName = "e.bmp"


def entropy(bytes: bytes) -> float:
    occurances = {}
    total = 0
    for b in bytes:
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
    return -entr


def convert_to_RGB(data):
    pixels = []
    counter = 2

    for i in range(len(data) - 1):
        if counter == 2:
            r = int(data[i])
            g = int(data[i + 1])
            b = int(data[i + 2])

            pixels.append((r, g, b))
            counter = 0
        else:
            counter += 1
    return pixels


def brute_attack(cryptogram: bytes, iv: bytes):
    de = 3
    length = 3
    alphabet = string.ascii_lowercase
    for password in passwordGenerator(length, alphabet):
        key = PBKDF2(password, b'abc')

        aes = AES.new(key, AES.MODE_CBC, iv)
        decrypted = aes.decrypt(cryptogram)
        e = entropy(decrypted)
        print("{} -> {}".format(password, e))

        if e < de:
            print("Hasło: {}".format(password))

            print("Rysowanie")
            rgb = convert_to_RGB(decrypted)
            img_out = Image.new(img_in.mode, img_in.size)
            pix = img_out.load()
            for x in range(img_in.size[0]):
                for y in range(img_in.size[1]):
                    pix[x, y] = rgb[x + y * img_in.size[1]]
            img_out.show()
            break


img_in = Image.open(fileName)
print(img_in.mode)
print(img_in.size)
data = img_in.convert("RGB").tobytes()
brute_attack(data, get_random_bytes(16))
