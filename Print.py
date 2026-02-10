# Comment

# Print
print("Hello World")


number, string, decimal, isTrue = 5, "Hello World", 3.14, True
name = "John"

# format
print("number: {}, string: {}, decimal: {} and isTrue: {}".format(number, string, decimal, isTrue))
# number: 5, string: Hello World, decimal: 3.14 and isTrue: True

print(name, string)     # John Hello World

print(name + string)     # JohnHello World

print(name + " " + string)      # John Hello World

print(name,"is a",string)       # John is a Hello World

# sep
print(name, string, sep="-")    # John-Hello World

# end
print(name, end="-")            # John-

# sep and end
print(number, string, decimal, isTrue, sep=" | ", end=" → Ends!\n")     # 5 | Hello World | 3.14 | True → Ends!

# f-string
print(f"number: {number}, string: {string}, decimal: {decimal} and isTrue: {isTrue}")   # number: 5, string: Hello World, decimal: 3.14 and isTrue: True






