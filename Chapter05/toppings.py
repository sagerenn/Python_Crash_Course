request_topping = 'mushrooms'
if request_topping != 'anchovies':
    print("Hold the anchovies")

print("haha")


a = 18
if a == 18:
    print("ok1")

if a != 18:
    print("ok2")

if a >= 18:
    print("ok3")

if a <= 18:
    print("ok4")

if a != 1:
    print("ok5")


age_0 = 35
age_1 = 40
if age_0 > 25 and age_1 > 25:
    print("hahhaa")

if age_0 < 25 and age_1 > 25:
    print("hahhaa2")

if age_0 != 25 and (age_1 < 25):
    print("hahhaa2")

if age_0 != 25 or (age_1 < 25):
    print("hahhaa2")

request_toppings = ['mushrooms','onions','pipeapple']
if 'mushrooms' in request_toppings:
    print("OK")
else:
    print("KO")

if 'meat' in request_toppings:
    print("OK")
else:
    print("KO")


banned_users = ['andrew', 'carolina', 'david']
user = "jonna"
if user not in banned_users:
    print(f"{user.title()} can post a comment!")

a = (2>3)
if a == True:
    print("True")
else:
    print("False")


car = 'subaru'
print("Is car is audi? I predict True")
print(car == 'audi')
print("Is car is subaru? I predict True")
print(car == 'subaru')

a = ['sdf']
print("The list can be compared.")
print(a == ['sdf'])
print(a[0] == "sdf")
print(a[0] != "sdf")

b = 100
print(b>1000)
print(b!= 0)

print(a[0] == b)
print(a[0] != b)
print(a[0] != "SDF".lower())
print(a[0] == "SDF".lower())

if a[0] == "sdf" and b < 1000:
    print("sdferg")


if a[0] == "sdf" or b > 1000:
    print("sdferg")

print("sdf" in a)
print("sdf" not in a)


request_toppings = ['mushrooms','onions','pipeapple']
for request_topping in request_toppings:
    print(f"Adding {request_topping}")
print("\nFinished making your pizza!")

request_toppings = ['mushrooms','onions','pipeapple']
for request_topping in request_toppings:
    if request_topping == 'onions':
        print(f"Sorry, we are out of {request_topping} right now!")
    else:
        print(f"Adding {request_topping}")
print("\nFinished making your pizza!")

print("-------------------")
request_toppings = []
for request_topping in request_toppings:
    if request_topping == 'onions':
        print(f"Sorry, we are out of {request_topping} right now!")
    else:
        print(f"Adding {request_topping}")

if request_toppings:
    for request_topping in request_toppings:
        if request_topping == 'onions':
            print(f"Sorry, we are out of {request_topping} right now!")
        else:
            print(f"Adding {request_topping}")
else:
    print("Are you sure you want a plain pizza?")



print("-------------------")
request_toppings = ['sdf']
for request_topping in request_toppings:
    if request_topping == 'onions':
        print(f"Sorry, we are out of {request_topping} right now!")
    else:
        print(f"Adding {request_topping}")

if request_toppings:
    for request_topping in request_toppings:
        if request_topping == 'onions':
            print(f"Sorry, we are out of {request_topping} right now!")
        else:
            print(f"Adding {request_topping}")
else:
    print("Are you sure you want a plain pizza?")

print("-------------------")
avaiable_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','frensh fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in avaiable_toppings:
        print(f"adding {requested_topping}")
    else:
        print(f"It's unavailable topping!")

print("\nIs it ok?")