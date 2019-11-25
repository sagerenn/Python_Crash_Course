aliens = []

for i in range(1,30):
    print(i,sep=" ",end=" ")

print()

for i in range(30):
    aliens.append({'color':'green', 'points': 5, \
        'speed': 'slow', 'position': i})

for alien in aliens[:5:2]:
    print(alien)
print("...")

print(f"The number of aliens: {len(aliens)}")



aliens = []


for i in range(30):
    aliens.append({'color':'green', 'points': 5, 'speed': 'slow'})

# print(set(aliens))
# Exception has occurred: TypeError
# unhashable type: 'dict'

for alien in aliens[:3]:
    if alien['speed'] == "slow":
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'
    elif alien['speed'] == "medium":
        alien['color'] = 'red'
        alien['points'] = '15'
        alien['speed'] = 'high'

print(aliens[:5])

pizza = {
    "crust": "thick",
    "toppings": ['mushrooms','extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza"
    " with the following toppings: {pizza['toppings']}")


favorite_languages = {
    "susan": ['python',"c","java"],
    "hedy": ['python'],
    "joanna": ['python','php']
}

for name,languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"{name}'s favorite language are: ")
        for language in languages:
            print(f"\t{language}")
    else:
        print(f"{name}'s favorite language is {languages[0]}")
        


users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

print(users['mcurie']['location'])


print("------------------------------")
for use,info in users.items():
    for k,v in info.items():
        if k == 'first':
            print(f"The {use}'s first name: {v.title()}")
        elif k == 'last':
            print(f"The {use}'s last name: {v.title()}")
        elif k == 'location':
            print(f"The {use}'s location: {v.title()}")