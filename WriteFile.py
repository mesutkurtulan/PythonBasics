file = open("writefile.txt")

file.close()

# instead of manually closing file, we can use
with open("writefile.txt", "r") as reader: # r = read mode, w = write mode
    content = reader.readlines()
    with open("writefile.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)