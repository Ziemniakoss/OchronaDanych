from getpass import getpass
from hashlib import md5
import htpasswd

print("Login: ", end="")
login = input()
print("Hasło: ", end="")
password = getpass()

with htpasswd.Basic("password.txt", mode="md5") as userdb:
    try:
        userdb.add(login, password)
        print("Ok")
    except Exception:
        print("error")
