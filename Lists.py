# List

numbers = range(5)
print(numbers)              # range(0, 5)
print(numbers[0])           # 0

numbers = [0, 1, 2, 3, 4, 5]
print(numbers)              # [0, 1, 2, 3, 4, 5]
print(numbers[0])           # 0
print(numbers[1:3])         # [1, 2]

# insert(i, x)
numbers.insert(6, 6)
print(numbers)              # [0, 1, 2, 3, 4, 5, 6]

# append(x)
numbers.append(7)
print(numbers)              # [0, 1, 2, 3, 4, 5, 6, 7]

#extend(iterable)
numbers.extend([8, 9])
print(numbers)              # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers[7] = -7
print(numbers)              # [0, 1, 2, 3, 4, 5, 6, -7, 8, 9]

del numbers[7]
print(numbers)              # [0, 1, 2, 3, 4, 5, 6, 8, 9]

numbers.remove(8)
print(numbers)              # [0, 1, 2, 3, 4, 5, 6, 9]

numbers.pop(7)
print(numbers)              # [0, 1, 2, 3, 4, 5, 6]

print(numbers.index(6))     # 6

print(numbers.count(6))     # 1

numbers.reverse()
print(numbers)              # [6, 5, 4, 3, 2, 1, 0]

numbers.sort()
print(numbers)              # [0, 1, 2, 3, 4, 5, 6] old list

newNumbers = sorted(numbers)
print(newNumbers)           # [0, 1, 2, 3, 4, 5, 6] new list

print(len(numbers))         # 7