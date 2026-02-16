fruits = ["apple", "pearl", "banana", "strawberry"]
fruits_uppercase = []

for fruit in fruits:
    fruits_uppercase.append(fruit.upper())

print(fruits_uppercase)  # ['APPLE', 'PEARL', 'BANANA', 'STRAWBERRY']

fruits = ["apple", "pearl", "banana", "strawberry"]
fruits_uppercase = [fruit.upper() for fruit in fruits]
print(fruits_uppercase)  # ['APPLE', 'PEARL', 'BANANA', 'STRAWBERRY']

# Only the squares of even numbers
squares_of_even_numbers = [x**2 for x in range(1, 21) if x % 2 == 0]
print(squares_of_even_numbers)  # [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

# "Multiply only the numbers from 1 to 15 that are divisible by 3 by 10 and add them to the list."
# Expected output approximately: [30, 60, 90, 120, 150]

print([x*10 for x in range(1, 16) if x%3 == 0])

