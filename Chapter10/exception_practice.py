import os


def read_text(dir_path, file_list):
    """read a list of file"""
    for file in file_list:
        try:
            with open(dir_path + '/' + file) as f:
                contents = f.read()
        except FileNotFoundError:
            pass
            # print(f"The {file} is missing")
        else:
            print(contents.strip())


dir_path = os.path.dirname(__file__)
file_list = ['cats.txt', 'dogs.txt']
read_text(dir_path, file_list)

with open(dir_path + '/dogs.txt', 'w') as f:
    f.write('ja\n')
    f.write('df\n')
    f.write('dsf\n')

read_text(dir_path, file_list)
os.remove(dir_path + '/dogs.txt')

with open(dir_path + '/' + 'the_good_work.txt') as f:
    print(f"There are about {f.read().lower().count('the ')} times of 'the'")

while True:
    try:
        first_number = int(input("the first number: "))
        second_number = int(input("the second number: "))
    except ValueError:
        print("Please enter the correct number")
    else:
        print(first_number + second_number)