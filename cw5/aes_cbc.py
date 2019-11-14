from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from multiprocessing import Pool, RawArray
import ctypes
import time

blockSize = 16
processes = 16
plainText = "lghalhglhlghlahgla" * blockSize * 1000000
password = "1234567890123456"
iv = get_random_bytes(16)


def xor(a: bytearray, b: bytearray) -> bytes:
    return bytes(a[i] ^ b[i] for i in range(len(a)))


def decrypt():
    with Pool(processes) as p:
        p.map(CBC_decrypt_block, range(len(encrypted) // blockSize))
    return bytes(decrypted)


def CBC_decrypt_block(n: int) -> None:
    vector = iv if n == 0 else bytes(encrypted[(n - 1) * blockSize: n * blockSize])

    block = bytes(encrypted[n * blockSize: (n + 1) * blockSize])

    x = aes.decrypt(block)
    decrypted[n * blockSize: (n + 1) * blockSize] = bytes(xor(x, vector))


encrypted = AES.new(password, AES.MODE_CBC, iv).encrypt(plainText)
decrypted = RawArray(ctypes.c_ubyte, bytearray([0] * len(encrypted)))

aes = AES.new(password)
start = time.time()
for i in range(26000):
    recovered = decrypt()
print(f'Deszyfrowanie zajęło {(time.time() - start)}')

print(recovered.decode()[:100])
