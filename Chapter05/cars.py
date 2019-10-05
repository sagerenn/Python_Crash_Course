cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


car = "audi"
if car == "audi":
    print("ok")
else:
    print("ko")

if car == "Audi":
    print("ok")
else:
    print("ko")

if car.title() == "Audi":
    print("ok")
else:
    print("ko")

