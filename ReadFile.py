txtFile = open("readfile.txt")

# Read all file
# print(txtFile.read())       #Line1, Line2, Line3, Line4, Line5

# Read number of character
# print(txtFile.read(2))      #Li

# Read One Single Lne
# print(txtFile.readline())       # Line1
# print(txtFile.readline())       # Line2

# Print Line by Line
"""
for line in txtFile:
    print(line)
"""

lines = txtFile.readlines()
print(lines)                    # ['Line1\n', 'Line2\n', 'Line3\n', 'Line4\n', 'Line5']

txtFile.close()