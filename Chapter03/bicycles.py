a="test"
b="redline"
c="trek"
d = [a,b,c,"cannondale",6]
print(d)
print(d[4]+7)
print(d[0].title())

# return the item of the list from the right to left
print(d[-1])
print(d[-2])
print("The bicycle is {}".format(d[3].title()))


names = ['susan','joanna','hedy']
print(names)
print(names[0].title(),names[1].title(),names[2].title())
message="Hi {}, How are you?".format(names[0].title())
print(message)

message=f"Hi {names[1].title()}, How are you?"
print(message)

print(f"Hi {names[2].title()}, How are you?")

transportation=["car","trunk","plane"]
print(f"I would like to own a {transportation[2]}")

# >>> a=['4',4,5]
# >>> a
# ['4', 4, 5]
# >>> a[0]=2
# >>> a
# [2, 4, 5]
# >>> a[0]+7
# 9
# >>> 

transportation.append("bicycle")
print(transportation.append("bicycle"))
a="motor"
transportation.append(a)
print(transportation)

transportation.append(names)
print(transportation)
# ['car', 'trunk', 'plane', 'bicycle', 'bicycle', 'motor', \ 
# ['susan', 'joanna', 'hedy']]
print(transportation[-1][2])

transportation.insert(1,"train")
print(transportation)

del transportation[1]
print(transportation)

# a = 'tr'
# print(a)

# del a
# print(a)


poped_name = names.pop()
print(names)
print(poped_name)

# ['susan', 'joanna']
# hedy

poped_name = names.pop(0)
print(names)
print(poped_name)

# ['joanna']
# susan

print(transportation.remove("car"))
print(transportation)

# ['trunk', 'plane', 'bicycle', 'bicycle', 'motor', ['joanna']]

b = ['joanna']
transportation.remove(b)
print(f"remove {b}, remain {transportation}")

transportation.append("car")
transportation.insert(-3,"car")
print(transportation)

transportation.remove("car")
print(transportation)


friend_list = ['susan','joanna','hedy']
print(f"hello {friend_list[0]}, would you like to have dinner with me?".title())

busy_friend = friend_list[0]
friend_list[0] = 'mary'
print(f'{busy_friend} cannot come,  the new list is {friend_list}')

friend_list.append("Mike")
friend_list.insert(0,"John")
friend_list.insert(3,"Sage")
print(friend_list)

first = friend_list.pop()
second = friend_list.pop(2)
friend_list.remove("mary")
print(friend_list,first, second)
del friend_list[0]
del friend_list[0]
del friend_list[0]

print(friend_list)