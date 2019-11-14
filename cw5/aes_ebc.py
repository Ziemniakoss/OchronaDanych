import time
from multiprocessing import Pool
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

blockSize = 16
processes = 32
plainText = "abcdefglopiasdcg" * blockSize * 90000
password = "1234567890123456"
textLen = len(plainText)
aes = AES.new(password, AES.MODE_ECB, get_random_bytes(blockSize))


def encrypt_parrell():
    result = None
    with Pool(processes) as p:
        result = p.map(encrypt_block, range(0, textLen, blockSize))
    return result


def encrypt_block(start: int):
    enc: str
    if start + blockSize > textLen:
        enc = plainText[start:start + blockSize] + (" " * (textLen - start + 1))
    else:
        enc = plainText[start:start + blockSize]
    return aes.encrypt(enc)


def decrypt_parrell(data):
    with Pool(processes) as p:
        result = p.map(decrypt_block, data)
    return result


def decrypt_block(block):
    return aes.decrypt(block)


def encrypt():
    v = bytearray(plainText, "utf-8")
    aes = AES.new(password, AES.MODE_ECB)
    for i in range(0, len(plainText), blockSize):
        v[i:i + blockSize] = aes.encrypt(plainText[i:i + blockSize])
    return v


def decrypt(enc: bytearray):
    v = bytearray(enc)
    aes = AES.new(password, AES.MODE_ECB)
    for i in range(0, len(plainText), blockSize):
        v[i:i + blockSize] = aes.decrypt(plainText[i:i + blockSize])
    return v


s = time.time()
e = encrypt_parrell()
print(f'Szyfrowanie równoległe: {time.time() - s}')
s = time.time()
decrypt_parrell(e)
print(f'Deszyfrowanie równoległe: {time.time() - s}')

s = time.time()
e = encrypt()
print(f'Szyfrowanie: {time.time() - s}')
s = time.time()
decrypt(e)
print(f'Deszyfrowanie: {time.time() - s}')
