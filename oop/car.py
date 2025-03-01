class Car:
    def __init__(self, modelname, year, mileage_kmpl):
        self.modelname = modelname
        self.year = year
        self.mileage_kmpl = mileage_kmpl
    def convert_to_mpg(self):
        return self.mileage_kmpl * 0.354006
    def format_output(self):
        return f"The {self.year} {self.modelname} combines exhilarating performance with a fuel-efficient mileage of {self.convert_to_mpg()} mpg, offering an iconic driving experience for enthusiasts and commuters alike."
    
car = Car("Ford Mustang GT", 2024, 10)
print(car.format_output())