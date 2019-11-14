from hashlib import md5
import sys


def md5sum(fileName: str) -> str:
    with open(fileName, "rb") as file:
        h = md5(file.read()).hexdigest()
    return h


for i in range(1, len(sys.argv)):
    f = sys.argv[i]
    print("{} {}".format(md5sum(f), f))
