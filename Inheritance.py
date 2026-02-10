class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def runVehicle(self):
        print(self.brand, self.model)

class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.year = year

    def runVehicle(self):
        super().runVehicle()
        print(self.year)

class ElectricCar(Car):
    def __init__(self, brand, model, year, milage):
        super().__init__(brand, model, year)
        self.milage = milage

    def runVehicle(self):
        super().runVehicle()
        print(self.milage)

tesla = ElectricCar('tesla', 'model s', 2016, 10000)
tesla.runVehicle() # tesla model s # 2016 # 10000


