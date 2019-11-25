def make_shirt(size='large',message='I love Python'):
    print(f"you require the {size} size of shirt, the words, '{message}' on it.")

make_shirt('middle','hahah')
make_shirt(size='small',message='susan')
make_shirt()
make_shirt('medium')
make_shirt(message='df')

def describe_city(city,country='China'):
    print(f"{city}--{country}")

describe_city("guangzhou")
describe_city("quanzhou")
test = describe_city("New York","USA")
print(test)


def get_formatted_name(first_name,last_name):
    return("{} {}".format(first_name,last_name).title())

get_formatted_name("susan","zeng")
full_name = get_formatted_name("joanna","zhang")
print(full_name)


def get_formatted_name(first_name,last_name,middle_name = ''):
    """return a full name, neatly formatted"""
    if middle_name:
        return("{} {} {}".format(first_name,middle_name,last_name).title())
    else:
        return("{} {}".format(first_name.title(),last_name.title()))

full_name = get_formatted_name("joanna","zhang")
print(full_name)
full_name = get_formatted_name("joanna","zhang","r")
print(full_name)


def build_person(first_name,last_name,age=None):
    person = {'first':first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix')
print(musician)
musician = build_person('jimi','hendrix',23)
print(musician)