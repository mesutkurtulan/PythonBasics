'''
Create a variable named greeting and assign it the string "Welcome to Python Programming".
Print the greeting variable.
Modify the string to include your instructor name "Rahul!". For example, "Welcome to Python Programming, [Instructor Name]!" and print the modified string.
'''

greeting = "Welcome to Python Programming"
greeting_with_name = "Welcome to Python Programming, Rahul!"
print(greeting_with_name)

'''
Create three variables: age, height, and favorite_color. Assign them values 25, 5.9, blue:
age: an integer (e.g., 25)
height: a float (e.g., 5.9)
favorite_color: a string (e.g., "blue")
Use the print function to display each variable and its type using the type() function.
'''
age, height, favorite_color = 25, 5.9, "blue"
print(f"Age: {age} | Type: {type(age)}")
print(f"Height: {height} | Type: {type(height)}")
print(f"Favorite Color: {favorite_color} | Type: {type(favorite_color)}")

'''
Create a list named fruits that contains below five different fruit names (strings).
"apple", "banana", "cherry", "date", "elderberry"
Print the first and last elements of the list.
Use slicing to print the second and third fruits from the list.
'''
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Fruits from index 1 to 2: {fruits[1:3]}")

'''
Create a tuple named person that contains three elements: a name (string), an age (integer), and a height (float) with the below values.
"Rahul", 25, 5.9
Print the second element of the tuple.
'''
person= ("Rahul", 25, 5.9)
print(f"Age: {person[1]}")

'''
Create a dictionary named car with the following keys: make, model, year, and color. Assign appropriate values to each key.
    "make": "Toyota",
    "model": "Camry",
    "year": 2020,
    "color": "Blue"
Print the value associated with the model key.
Add a new key called owner and assign it the name "Rahul".
Print the entire dictionary.
'''
car = {
    "make": "Toyota",
    "model": "Camry",
    "year": 2020,
    "color": "Blue"
}
print("Car model:", car.get("model"))
car["owner"] = "Rahul"
print("Updated car dictionary:", car)

'''
Write a program that assigns a greeting to a variable.
Use an if statement to check if the greeting is "Hello".
If it matches, print "Hello there!" and "How can I assist you today?".
If it does not match, print "Greetings!".
After the if-else block, print "Program has completed."
'''
greeting = "Hello"
if greeting == "Hello":
    print("Hello there!")
    print("How can I assist you today?")
    print("Program has completed.")
else:
    print("Greetings!")
    print("Program has completed.")

'''
Create a variable b and assign it a number 15.
Write an if statement to check if b is greater than 10.
If true, print "Number is greater than 10".
If false, print "Number is 10 or less".
Print "Comparison code is completed." at the end.
'''
b = 15
if b >= 10:
    print("Number is greater than 10")
    print("Comparison code is completed.")
else:
    print("Number is 10 or less")
    print("Comparison code is completed.")

'''
Create a list of numbers: [1, 4, 7, 10].
Use a for loop to iterate through the list.
Inside the loop, print each number multiplied by 3.
'''
numbers = [1, 4, 7, 10]
for number in numbers:
    print(number*3)

'''
Create a variable user and assign the value 16
Use if-elif-else statements to print:
"Good Morning" if the hour is between 5 and 11,
"Good Afternoon" if the hour is between 12 and 17,
"Good Evening" if the hour is between 18 and 21,
"Good Night" for all other hours.
Print "Greeting code has completed."
'''
user = 16
if 5 <= user <= 11:
    print("Good Morning")
    print("Greeting code has completed.")
elif 12 <= user <= 17:
    print("Good Afternoon")
    print("Greeting code has completed.")
elif 18 <= user <= 21:
    print("Good Evening")
    print("Greeting code has completed.")
else:
    print("Good Night")
    print("Greeting code has completed.")

'''
Create a class named BasicCalculator.
Define a constructor that initializes two numbers. Use numbers 10 & 5
Implement methods for:
Addition
Subtraction
Multiplication
Division
Each method should return the result of the operation.
Create an instance of the BasicCalculator class and demonstrate the functionality of each method.
'''
class BasicCalculator:
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
    def addition(self):
        return self.firstNumber + self.secondNumber
    def subtraction(self):
        return self.firstNumber - self.secondNumber
    def multiplication(self):
        return self.firstNumber * self.secondNumber
    def division(self):
        if self.secondNumber != 0:
            return self.firstNumber / self.secondNumber
        else:
            return "Division by zero is not allowed."

calc = BasicCalculator(10, 5)
print("Addition:", calc.addition())
print("Subtraction:", calc.subtraction())
print("Multiplication:", calc.multiplication())
print("Division:", calc.division())

'''
Write a function called GreetUser that takes a single argument username.
The function should print "Hello, [username]! Welcome to the Python course."
Call the function with username "John".
'''
def GreetUser(username):
    print(f"Hello, {username}! Welcome to the Python course.")
GreetUser("John")

'''
Create a function called CalculateAverage that takes three parameters: num1, num2, and num3.
Use the numbers 10,20,30 as input to functions
The function should return the average of these three numbers.
'''
def CalculateAverage(num1, num2, num3):
    return (num1 + num2 + num3) / 3
print(f"The average of 10, 20, and 30 is {CalculateAverage(10, 20, 30)} ")

'''
Sample file file1.txt is provided with this assignment.
Write a Python script that opens the file and reads all its contents.
Print the entire content of the file.
'''
file = open("file1.txt")
print(file.read())

'''
Use the attached text file "file1.txt"
Write a Python script that opens the file, reads through it line by line, counts how many lines it has, and prints the total count.
'''
file = open("file1.txt")
totalnumberoflines = 0
for line in file:
    totalnumberoflines += 1
print(f"Total number of lines: {totalnumberoflines}")

'''
Create a variable ItemsInCart and initialize it to 0.
Write a function called add_to_cart that accepts an integer parameter items_to_add.
If items_to_add is less than 0, raise an exception with the message "Cannot add a negative number of items."
If the total count of items after addition exceeds 5, raise an exception with the message "Cart limit exceeded."
'''
ItemsInCart = 0
def add_to_cart(items_to_add):
    global ItemsInCart
    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")

    if ItemsInCart + items_to_add > 5:
        raise Exception("Cart limit exceeded.")

    ItemsInCart += items_to_add
    print(f"{items_to_add} items added. Total in cart: {ItemsInCart}")

try:
    add_to_cart(2)
    add_to_cart(-1)
except Exception as e:
    print(e)

'''
Create a tuple named person that contains three elements: a name (string), an age (integer), and a height (float) with the below values.
"Rahul", 25, 5.9
Print the second element of the tuple.
Attempt to change the name in the tuple to a different name and explain why this will or will not work.
'''
person = ("Rahul", 25, 5.9)
print(f"Age: {person[1]}")
try:
    person[0] = "John"
except Exception as e:
    print(f"Error: {e} - Tuples are immutable.")