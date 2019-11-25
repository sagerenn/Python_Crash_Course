import json
import os

dir_path = os.path.dirname(__file__)
file_name = 'numbers.json'
numbers = [2,4,6,8,9,4]
info = {
    'user_name': 'susan',
    'location': 'gz'
}

def get_stored_name(file_name):
    """Get stored username if available"""
    try:
        with open(file_name) as f:
            contents = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return contents

def save_username(file_name):
    user_name = input("What's your name? ")
    with open(file_name, 'w') as f:
        json.dump(user_name, f)
    return user_name

def greeting_user(file_name):
    """Greet the user by name."""
    user_name = input("What's your name? ")
    username = get_stored_name(file_name)
    if username == user_name:
        print(f"Welcome back, {username}!")
    else:
        print("You are a new user!")
        user_name = save_username(file_name)
        print(f"We'll remember you when you come back, {user_name}!")

def greet_user():
    """
    we don't need to check first, just focus the main part and handle the error
    """
    try:
        with open(dir_path + '/' + file_name) as f:
            contents = json.load(f)
            # contents = f.read() # return as string
    except FileNotFoundError:
        user_name = input("What's your name? ")
        with open(dir_path + '/' + file_name, 'w') as f:
            # f.write(numbers.__str__())
            # f.write(info.__str__())
            # json.dump(numbers, f)
            # json.dump(info, f)
            json.dump(user_name, f)
    else:
        print(contents)

# greet_user()
greeting_user(dir_path + '/' + file_name)


def ask_favorite_number(file_name):
    """ask the user to enter their favorite number"""
    try:
        favorite_number = int(input("What's your favorite number? "))
        with open(file_name, 'w') as f:
            json.dump(favorite_number, f)
    except:
        print("Please enter the correct number!")
        favorite_number = ask_favorite_number(file_name)
    finally:
        return favorite_number

def get_stored_info(file_name):
    """get the stored infomation"""
    try:
        with open(file_name) as f:
            contents = int(json.load(f))
    except:
        return None
    else:
        return contents

def poll_number(file_name):
    """check the favorite number!"""
    favorite_number = get_stored_info(file_name)
    if favorite_number:
        print(f"your favorite number is {favorite_number}")
    else:
        print(f"I will remember {ask_favorite_number(file_name)}")

# poll_number(dir_path + '/' + file_name)