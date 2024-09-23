class Vehicle
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.available = True
    
    def sell(self):
        if self.available:
            self.available = False
            print(f"The car {car.make} has been sold")
        else:
            print(f"The car {car.make} is not available")
    
    def __str__(self):
        return f'{self.make}'