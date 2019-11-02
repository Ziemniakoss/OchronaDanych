import hashlib

bytesChecked = 32
original = open("original.html", "rb")
copy = open("copy.html", "rb")

hashOriginal = hashlib.sha3_256(original.read(bytesChecked)).hexdigest()
hashCopy = hashlib.sha3_256(copy.read(bytesChecked)).hexdigest()
print("SHA orginału: ", hashOriginal)
print("SHA kopi:     ", hashCopy)
if hashCopy == hashOriginal:
    print("Zgadzają się")
else:
    print("NIe zgadzają się")
