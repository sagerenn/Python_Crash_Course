def greet_users(names):
    """print a simple greeting to each user in the list"""
    for name in names:
        print("Hi {}".format(name).title())

names = ['susan','hedy','joanna']
greet_users(names)

names = 'test'
greet_users(names)

def verified_list(prepared_list,finish_list):
    while prepared_list:
        prepared_item = prepared_list.pop(0)
        print(f"Printing {prepared_item.title()}")
        finish_list.append(prepared_item)

def print_list(list):
    for item in list:
        print(item)

unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []
# verified_list(unprinted_designs[:],completed_models)
verified_list(unprinted_designs.copy(),completed_models)
print("These designs are printed: ")
print_list(completed_models)
print(unprinted_designs)


def show_messages(list):
    for msg in list:
        print(msg)

msg_list = ['Hi','susan']
show_messages(msg_list)

def show_messages(list,list2):
    while list:
        item = list.pop(0)
        print(item)
        list2.insert(len(list2),item)

msg_list = ['Hi','susan']
msg_list2 = []
show_messages(msg_list[:],msg_list2)
print(msg_list,msg_list2)
show_messages(msg_list,msg_list2)
print(msg_list,msg_list2)


tuple_list = ('haha',['shsh'])
tuple_list[1][0] = 'sdf'
print(tuple_list)

def make_pizza(test, *toppings, yesy, base = 'cheese'):
    print(toppings)
    print(base)

make_pizza('mushroom','pineapple',yesy='sdf')


def build_profile(first_name,last_name,**user_info):
    """build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info

user_profile = build_profile("susan","zeng",location = 'guangzhou',field='manager')
print(user_profile)


def make_sandwich(*materials):
        print(materials)

make_sandwich('fish','bread','vegetables')
make_sandwich('fish','meat')

user_profile = build_profile("susan","zeng",job = 'none')
print(user_profile)

def make_car(manufacturer,model,**car_info):
        car_info['manufacturer'] = manufacturer
        car_info['model'] = model
        return car_info

print(make_car('subaru','outback',color = 'blue', tow_package = True))