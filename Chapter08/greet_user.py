def greet_user(username):
    """
    sdf
    sdjfosdf
    g56y76i\"
    """
    print(f"Hello! {username.title()}")

greet_user('susan')
print(greet_user.__doc__)


def display_message():
    print("I have learned the function of Python!")

display_message()

def favorite_book(title):
    print(f"The {title.title()} is one of my favorite books!")

favorite_book("Alice in Wonderland")


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster','harry')
describe_pet(pet_name='willie',animal_type='dog')


def describe_pet(pet_name,animal_type = 'dog'):
    """Display information about a pet."""
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet(pet_name='willie')
describe_pet('willie','sdf')
describe_pet(pet_name='harry',animal_type='hamster')


def get_formatted_name(first_name, last_name):
    full_name = "{} {}".format(first_name,last_name).title()
    return full_name

while True:
    first_name = input("Your first name: ")
    last_name = input("Your last name: ")
    full_name = get_formatted_name(first_name,last_name)
    print(f"Hi {full_name}, There is a meeting at 10 a.m.")
    if input("Do you want to continue?(yes/no)").lower() == 'no':
        break

