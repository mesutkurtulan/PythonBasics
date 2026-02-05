# List

numbers = range(5)
print(numbers)              # range(0, 5)
print(numbers[0])           # 0

numbers = [0, 1, 2, 3, 4, 5]
print(numbers)              # [0, 1, 2, 3, 4, 5]
print(numbers[0])           # 0
print(numbers[1:3])         # [1, 2]

numbers.insert(6, 6)
print(numbers)              # [0, 1, 2, 3, 4, 5, 6]

numbers.append(7)
print(numbers)              # [0, 1, 2, 3, 4, 5, 6, 7]

numbers[7] = -7
print(numbers)              # [0, 1, 2, 3, 4, 5, 6, -7]

del numbers[7]
print(numbers)              # [0, 1, 2, 3, 4, 5, 6]