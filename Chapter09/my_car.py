import car_class

my_new_car = car_class.Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())



my_new_car.odometer_reading = 23
print(my_new_car.get_descriptive_name())


import car_class as CC


my_new_car_5 = CC.Car('audi', 'a5', 2019)
print(my_new_car_5.get_descriptive_name())


from car_class import Car

my_new_car_2 = Car('audi', 'a4', 2018)
print(my_new_car_2.get_descriptive_name())


from electric_car import ElectricCar

my_new_car_3 = ElectricCar('audi', 'a4', 2019, 150)
my_new_car_3.battery.get_battery_size()

from electric_car import ElectricCar as EC


my_new_car_6 = EC('audi', 'a4', 2019, 200)
my_new_car_6.battery.get_battery_size()


from electric_car import *

my_new_car_4 = Battery(350)
my_new_car_4.get_battery_size()