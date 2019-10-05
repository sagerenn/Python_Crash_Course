person = 'eric'
print("Hello {}, would you like to learn some \
     Python today?".format(person.title()))
print(f'Hello {person.title()}, would you like to learn some Python today?')

print(person.lower())
print(person.upper())

famous_person="albert einstein"
print(f'{famous_person} once said, "A person who never make a \
    mistake never tried anything new."')

person_with_whitespace = '\tJoanna Zhang\n'
print(person_with_whitespace.strip())
print(person_with_whitespace.lstrip())
print(person_with_whitespace.rstrip())