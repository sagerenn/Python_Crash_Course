import os

dir_path = os.path.dirname(__file__)
file_path = dir_path + '/guest.txt'

while True:
    user_name = input("What's your name? ")
    reason = input("Why do you like programming? ")
    print(f"Hi, {user_name}")
    with open(file_path, 'a') as file_object:
        file_object.write(user_name + ': ' + reason + '\n')

    with open(file_path) as file_object:
        print(file_object.read().strip())

    if input("continue?(yes/no) ").lower() == 'no':
        break
