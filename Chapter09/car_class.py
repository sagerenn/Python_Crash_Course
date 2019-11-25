"""A class that can be used to represent a car."""

class Car:
    """a simple attempt to represent a car."""

    def __init__(self, make, model, year, odometer_reading=0):
        """initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading

    def get_descriptive_name(self):
        """retuen a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model} {self.odometer_reading}"
        return long_name.title()

    def update_odometer(self,mileage):
        """Set the odometer reading to the given value"""
        if self.odometer_reading >= mileage:
            print("Please don't roll back the mileage!")
        else:
            self.odometer_reading = mileage

    def increment_odometer(self,add_mileage):
        """add the mileage to the whole"""
        self.odometer_reading += add_mileage

    def fill_gas_tank(self, gas_tank):
        """set the volumn of gas added to tank"""
        self.gas_tank = gas_tank


