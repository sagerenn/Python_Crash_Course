import os
import time
dir_path = os.path.dirname(os.path.realpath(__file__))

print(dir_path)
print(__file__)

with open(dir_path + '/pi_digits.txt') as file_object:
    for line in file_object:
        print(f"dd {line}")
    contents = file_object.read()

# contents = file_object.read()

print(contents.strip())

print("--------")

file_object_2 = open(dir_path + '/pi_digits.txt')
print(file_object_2.read())

print(file_object_2)

file_path = dir_path + '/pi_digits.txt'
with open(file_path) as file_object_3:
    for line in file_object_3:
        print(repr(f"dd {line}"))

print(file_object_3)

with open(file_path) as file_object_4:
    lines = file_object_4.readlines()


# time.sleep(30)

print(lines)
print(file_object_4)

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(float(pi_string))
print(complex(pi_string))
print(type(pi_string))
print(type(float(pi_string)))
print(len(pi_string))
print(len(str(float(pi_string))))
print(pi_string[:12])


pi_string_2 = ''
file_path = dir_path + '/pi_million.txt'
with open(file_path) as file_object_7:
    for line in file_object_7:
        pi_string_2 += line.strip()

your_birthday = input("your birthday, format mmddyy: ")
if your_birthday in pi_string_2:
    print("inside it")
else:
    print("outside it")

print(pi_string_2[:50])

i = 0

j = 0
for pi_char in pi_string_2:
    j += 1
    if pi_char == your_birthday[i]:
        i += 1
        if i == len(your_birthday):
            print(f"in the {j-2-3} position")
            break
    else:
        i = 0

