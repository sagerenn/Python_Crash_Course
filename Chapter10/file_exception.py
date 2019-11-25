import os

dir_path = os.path.dirname(__file__)
file_name = dir_path + '/alice.txt'
title = 'Alice in Wonderland\ntest\tferg'

# a variable defined outside cannot be used inside a fuction
def word_counter(file_name):
    """Count the approximate number of words in the file."""
    try:
        with open(file_name, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print("The text is missing!")
        pass
    else:
        file_name = os.path.basename(file_name)
        words = contents.split()
        print(f"{file_name} has about {len(words)} words!")
        # print(words)

word_counter(file_name)

with open(file_name, 'w') as f:
    f.write(title)

word_counter(file_name)

file_list = ['Bakers_Dozens.txt', 'the_good_work.txt','sdf.txt']

for file in file_list:
    word_counter(dir_path + '/' + file)

if 'sdf' == 'sdf':
    pass