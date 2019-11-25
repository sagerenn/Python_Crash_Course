"""A class that can be used to represent a eletric car."""

from car_class import Car

class Battery():
    """model a battery"""

    def __init__(self, battery_size):
        """initialize a battery"""
        self.battery_size = battery_size

    def get_battery_size(self):
        """print the battery size"""
        print(self.battery_size)

    def get_range(self):
        """print a statement about the range this battery provided"""
        if self.battery_size == 75:
            print("range: 260 miles")
        elif self.battery_size == 100:
            print("range: 315 miles")

    def upgrade_battery(self):
        """upgrade the battery size to 100 if it's not"""
        self.battery_size = 100


class ElectricCar(Car):
    """inherit the car class"""

    def __init__(self, make, model, year, battery_size):
        """
        initialize attributes of the parent class.
        specific the attribute to electric car
        """
        super().__init__(make, model, year)
        self.battery_size = battery_size
        self.battery = Battery(battery_size)

    def get_battery_size(self):
        """print the battery size"""
        print(self.battery_size)

    def fill_gas_tank(self): # the self will automatically pass
        """diable the method to electric car"""
        print("The electric car doesn't need the gas!")
