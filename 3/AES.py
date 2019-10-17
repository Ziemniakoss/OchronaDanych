import time
from Crypto.Cipher import DES, AES
from IPython.display import clear_output
from Crypto.Random import get_random_bytes

password = "key4567890123456"


def encode_file(inputFile: str, outputFile: str, key: str, mode):
    inputFile = open(inputFile, "rb")
    outputFile = open(outputFile, "wb")
    iv = get_random_bytes(16)
    aes = AES.new(key, mode, iv)
    while True:
        c = inputFile.read(16)
        if not c:
            break
        if len(c) != 16:
            a = bytes([ord('@')] * (16 - len(c)))
            c += a
        print(len(c))
        outputFile.write(aes.encrypt(c))
    outputFile.flush()
    outputFile.close()
    inputFile.close()


def decode_file(inputFile: str, outputFile: str, key: str, mode):
    inputFile = open(inputFile, "rb")
    outputFile = open(outputFile, "wb")
    iv = get_random_bytes(16)
    aes = AES.new(key, mode, iv)
    while True:
        c = inputFile.read(16)
        if not c:
            break
        if len(c) != 16:
            a = bytes([ord('@')] * (16 - len(c)))
            c += a
        print(len(c))
        outputFile.write(aes.decrypt(c))
    outputFile.flush()
    outputFile.close()
    inputFile.close()


encode_file("hamlet.txt", "hamlet_e.txt", password, AES.MODE_CBC)
decode_file("hamlet_e.txt", "hamlet_d.txt", password, AES.MODE_CBC)
