age = 19
if age>=18:
    print("You are old enough to vote!")
    print("Has you registered to vote yet?")

if age<=18:
    print("You are old enough to vote!")
else:
        print("sdfsdf")
print("hah")

if age >= 18:
    print("$40")
elif age < 18 and age >=4:
    print("$18")
else:
    print("free")

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age > 65:
    price = 20
else:
    price = 40

print(f"The price is {price}")


if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65 :
    price = 20

print(f"The price is {price}")


requested_toppings = ['mushrooms','pepperoni','extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("finish making your pizza!")


if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("finish making your pizza!")
    

alien_colors = ['green','red','yellow']
for alien_color in alien_colors:
    if alien_color == 'green':
        print("You earn 5 points!")
    elif alien_color == 'red':
        print("You dead!")
    elif alien_color == 'yellow':
        print("The alien is alive!")
    else:
        print("hahha")

age = 35

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
else:
    stage = 'elder'

print(stage.title())


favorite_foods = ['apple','pipeapple','banana']

if 'apple' in favorite_foods:
    print(f"I like apple")

if 'banana' in favorite_foods:
    print(f"I like banana")

food = 'cake'

if food in favorite_foods:
    print(f"I like {food}")

food = 'juice'

if food in favorite_foods:
    print(f"I like {food}")

food = 'pipeapple'

if food in favorite_foods:
    print(f"I like {food}")
