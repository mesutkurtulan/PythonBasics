# Else Elif Else

greeting = "Good morning"

if greeting == "Good afternoon":
    print("Good afternoon")
elif greeting == "Good evening":
    print("Good evening")
else:
    print("Good morning")

# For Loop

numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    print(number)

sumOfNumber = 0
for number in numbers:
    sumOfNumber += number

print(sumOfNumber)          # 21

sumOfNumber = 0
for number in range(1, 6):
    sumOfNumber += number

print(sumOfNumber)          # 15

for number in range(1, 11, 2): # 1, 3, 5, 7, 9
    print(number)

for number in range(10):  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    print(number)

# While Loop

count = 10
while count > 0:
    print(count)        # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    count -= 1

count = 0
while count < 10:
    if count % 2 == 0:
        print(count)
    count += 1

count = 1
while count <= 10:
    if count % 5 == 0:
        print(count)
        break
    count += 1

count = 1
while count <= 10:
    if count % 2 == 1:
        count += 1
        continue
    if count % 5 == 0:
        print(count)
        break
    count += 1