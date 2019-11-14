with open("test.txt", "r") as f:
    lines = f.readlines()
with open("test.txt", "w") as f:
    for line in lines:
        nick = line[0: (line.index(':'))]
        print(nick)
        if line.strip("\n") != "ma: afaf":
            f.write(line)