string1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
string2 = "consectetur adipiscing elit"
string3 = "Lorem ipsum"


print(string1[0])           # L
print(string1[0:5])         # Lorem -> substring
print(string1, string2)     # Lorem ipsum dolor sit amet consectetur adipiscing elit -> concatenation
print(string3 in string1)   # True -> substring check
print(string1.split(","))   # ['Lorem ipsum dolor sit amet', ' consectetur adipiscing elit']
print(string1.strip())      # "Lorem ipsum dolor sit amet, consectetur adipiscing elit" clear white spaces
print(string1.lstrip())     # "Lorem ipsum dolor sit amet, consectetur adipiscing elit" clear white spaces
print(string1.rstrip())     # "Lorem ipsum dolor sit amet, consectetur adipiscing elit" clear white spaces