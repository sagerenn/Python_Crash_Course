alient_0 = {'color': 'green', 'points': '5'}
print(alient_0['color'])
print(alient_0['points'])

alients = [{'color': 'green', 'points': '5'},\
            {'color': 'yellow', 'points': '10'},\
            {'color': 'red', 'points': '15'}]

shooted_alien = 'yellow'

for alient in alients:
    if alient['color'] == shooted_alien:
        print(f"You just earned {alient['points']} points!")


shooted_alien = 'red'
for i in range(0,len(alients)):
    if alients[i]['color'] == shooted_alien:
        print(f"You just earned {alient['points']} points!")



alient_0['x_position'] = 0
alient_0['y_position'] = 25
print(alient_0)


alient_0 = {}
alient_0['color'] = 'red'
alient_0['points'] = 15
print(alient_0)

alient_0['color'] = 'green'
print(alient_0)


food = {"meat":"fish"}
print(food['meat'])
food['meat'] = "crab"
print(food['meat'])

alient_0 = {
        'color': 'green',
        'x_position': 0,
        'y_position': 25,
        'speed': 'medium'
}

print(alient_0)

if alient_0['speed'] == 'slow':
        x_increment = 1
elif alient_0['speed'] == 'medium':
        x_increment = 2
elif alient_0['speed'] == 'high':
        x_increment = 3

alient_0['x_position'] += x_increment

print(alient_0,type(alient_0['x_position']))

del(alient_0['color'])
print(alient_0)

favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
}

print(favorite_languages)

favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python'
        }

print(favorite_languages)

print(f"I love {favorite_languages['phil'].title()}")

print(favorite_languages.get('susan','haha'))
print(favorite_languages.get('susan'))

if favorite_languages.get('susan') is None:
        print("chacha")

print(favorite_languages.get('phil'))


person = {
        "first_name": "Hedy",
        "last_name": "He",
        "age": "24",
        "city": "guangzhou",
}

print(person)


favorite_numbers = {
        "wangsu": 6,
        "wangsu2": 7,
        "wangsu3": 8,
        "wangsu4": 9,
        "wangsu5": 10,
}

for key, value in favorite_numbers.items():
        print(f"{key}: {value}")

print(f"dfgdfgdfg {favorite_numbers.get('wangsu10','sdferg')}")

programming_words = {
        "list": "the infomation stored in a object",
        "string": "a set of character",
        "condition": "if...elif..else",
        "dictionary": "associated array",
}

for key,value in programming_words.items():
        print(f"{key}\n\t{value}\n")
