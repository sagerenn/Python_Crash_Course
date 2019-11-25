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

my_new_car = Car('audi','a4',2019)
my_new_car.odometer_reading = 23
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(45)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(4)
print(my_new_car.get_descriptive_name())
my_new_car.increment_odometer(3_000)
print(my_new_car.get_descriptive_name())

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

my_tesla = ElectricCar('tesla', 's', 1990, 100)
print(my_tesla.get_descriptive_name())
my_tesla.get_battery_size()
my_tesla.fill_gas_tank()
my_tesla.battery.get_battery_size()
my_tesla.battery.get_range()
my_tesla.battery_size = 75
my_tesla.battery.get_range()
my_tesla.battery.battery_size = 75
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

