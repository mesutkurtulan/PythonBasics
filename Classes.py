class Calculator:
    number = 100

    def sum(self):
        print("Class Method Running")


# We are out of the class
calculatorObject = Calculator()
calculatorObject.sum()
print(calculatorObject.number)