import os

dir_path = os.path.dirname(__file__)

file_name = dir_path + '/python_learning.txt'

with open(file_name) as file_object:
    print(file_object.read().replace('Python','PHP'))

print("---------")

with open(file_name) as file_object:
    for line in file_object:
        print(line.strip().replace('Python','PHP'))

print("==========")

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip().replace('Python','PHP'))