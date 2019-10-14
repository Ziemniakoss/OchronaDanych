from Crypto.Cipher import ARC4


def str_to_int(string: str) -> list:
    l = []
    for char in string:
        l.append(ord(char))
    return l


def int_to_str(ints: list) -> str:
    result: str = ""
    for i in ints:
        result += chr(i)
    return result


def rc4_key(key: str) -> list:
    key = str_to_int(key)
    s = [i for i in range(256)]
    j = 0
    keyLen = len(key)
    for i in range(256):
        j = (j + s[i] + key[i % keyLen]) % 256
        s[i], s[j] = s[j], s[i]
    return s


def rc4_encode(message: str, key: str) -> str:
    s = rc4_key(key)
    message = str_to_int(message)
    result = ""

    i = 0
    j = 0
    for char in message:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        k = s[(s[i] + s[j]) % 256]
        result += chr(k ^ char)
    return result


while True:
    print("Wiadomosc: ", end="")
    message = input()
    print("Haslo: ", end="")
    password = input()
    encoded = rc4_encode(message, password)
    decoded = ARC4.new(password).decrypt(bytes(str_to_int(encoded)))
    print("Encoded: ", encoded)
    print("Decoded: ", decoded)
