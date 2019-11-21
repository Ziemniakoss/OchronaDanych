code = 1
length = 9
password = "a" * length
f = open("pass", "wb")
for i in range(length):
    f.write(code.to_bytes(4, "big"))
f.close()
