fileName = "password.txt"
print("Kogo usunąć? ", end="")
toRemove = input()
found = False
with open(fileName, "r") as f:
    lines = f.readlines()
with open(fileName, "w") as f:
    for line in lines:
        nick = line[0: (line.index(':'))]
        if nick != toRemove:
            f.write(line)
        else:
            found = True
if found:
    print("Usunieto")
else:
    print("Nie znaleziono użytkownika {}".format(toRemove))
