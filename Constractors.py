class Calculator:
    # default constructor
    def __init__(self):
        print("Default Constructor")

    num = 100   # class variables

    def sayHello(self):
        print("Hello World")

calcObj = Calculator()
print(calcObj.num)                              # Default Constructor # 100

# ----------------------------------- #
class Calculators:
    def __init__(self, num1, num2):
        self.num1 = num1                        # instance variable
        self.num2 = num2                        # instance variable
        print("Parametrized Constructor")

    number = 10    # class variables

    def multiplication(self):
        return (self.num1 * self.num2) + self.number - Calculators.number


calcObject1 = Calculators(2, 5)
print(calcObject1.number)                        # Parametrized Constructor # 10
print(calcObject1.multiplication())              # 10

calcObject2 = Calculators(4, 10)
print(calcObject2.number)                        # Parametrized Constructor # 10
print(calcObject2.multiplication())              # 40