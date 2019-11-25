user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

print(user_0.items())

for k,v in user_0.items():
    if k == "first":
        v = "sdfsdf"
    print("{}: {}".format(k,v))

print(user_0)

print(user_0.keys())
for k in user_0.keys():
    print(k.title())


for k in user_0:
    print(k.title())



favorite_languages = {
    "susan": "c",
    "hedy": "python",
    "joanna": "vc++"
}

friends = ['hedy','dfgg']

for friend in friends:
    if friend in favorite_languages:
        print(f"I see you love {favorite_languages[friend]}")
    else:
        print(f"Hi {friend}, What language do you love?")

for friend in friends:
    if friend in favorite_languages.keys():
        print(f"I see you love {favorite_languages[friend]}")
    else:
        print(f"Hi {friend}, What language do you love?")


for name,language in favorite_languages.items():
    if name in friends:
        print("Hi {}, I see you love {}".format(name,language))
    else:
        print(f"Hi {name}")

if 'erin' not in favorite_languages.keys():
    print("Please take our poll!")

print(favorite_languages.keys())



for name,language in sorted(favorite_languages.items(),reverse=True):
    print(f"{name.title()}: {language.title()}")

favorite_languages['le'] = "python"
for language in favorite_languages.values():
    print(language)

print("=========================")

for language in set(favorite_languages.values()):
    print(language)

favorite_languages = {
    "susan": "c",
    "hedy": "python",
    "hedy": "python",
    "joanna": "vc++"
}

print(favorite_languages)
print(set(favorite_languages.items()))


river_country = {
    "nile" : [' Tanzania', 'Uganda', 'Rwanda', 'Burundi', \
        'the Democratic Republic of the Congo', 'Kenya', 'Ethiopia', \
            'Eritrea', 'South Sudan', 'Republic of the Sudan and Egypt.'\
            ],
    "Amazon": ['Peru', 'Bolivia', 'Venezuela', 'Colombia', \
        'Ecuador', 'and Brazil '],
    "Yangtze": ["China"]
}

for river,country in river_country.items():
    print(f"{river}: {country}")
    print(f"{river}: {','.join(country)}")


for river in river_country.keys():
    print(f"{river.title()}")


for countrys in river_country.values():
    for country in countrys:
        print(f"{country.strip().title()}")


