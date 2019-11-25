import os 
import time

dir_path = os.path.dirname(__file__)

filename = dir_path + '/programming.txt'

with open(filename,'r+') as file_object:
    file_object.write('I love Python!')
    file_object.write('\nI love Python too!')
    file_object.flush() # why it write to file immediately?
    os.fsync(file_object)
    # time.sleep(5)
    print(file_object)
    print(file_object.read().strip())
    print(file_object.read().strip())

with open(filename) as file_object:
    print(file_object.read().strip())
    print(file_object)

with open(filename,'w') as file_object:
    file_object.write('\nI love Python too!')

with open(filename) as file_object:
    print(file_object.read().strip())
    print(file_object)

with open(filename,'w') as file_object:
    with open(filename) as file_object_2:
        print(file_object_2.read().strip())

with open(filename,'a') as file_object:
    file_object.write(str(3))

with open(filename,'a') as file_object:
    file_object.write(str(6) + "\n")
    file_object.write("sdfsdf")

with open(filename) as file_object:
    print(file_object.read().strip())
