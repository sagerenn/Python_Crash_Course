players = ['charles','martina','mechael','florence','eli']
print(players[:3])
print(players[2:])
print(players[-3:-1])
print(players[-3:0])
print(players[-3:1])

# the last three players
print(players[-3:])

print(players[1:-3])
print(players[1:4])

# specific the iterate
print(players[::2])
print(players[::])

# ['charles', 'martina', 'mechael']
# ['mechael', 'florence', 'eli']
# ['mechael', 'florence']
# []
# []
# ['mechael', 'florence', 'eli']
# ['martina']
# ['martina', 'mechael', 'florence']
# ['charles', 'mechael', 'eli']
# ['charles', 'martina', 'mechael', 'florence', 'eli']

for value in sorted(players[:3],reverse=True):
    print(value.title())

my_foods = ['pizza','falafel','cake']
# friend_foods = sorted(my_foods[:])
friend_foods = my_foods[:]
friend_foods.sort()
print(my_foods,friend_foods)
tmp1_foods = list(my_foods)
tmp2_foods = sorted(my_foods)


my_foods.append("sdf")
friend_foods.append("rgrtg")
tmp1_foods.insert(1,"rgtg")
print(my_foods,friend_foods,tmp1_foods,tmp2_foods)

for tmp3 in tmp2_foods:
    print(f"sdf {tmp3} weg")


print("The first three items in the list are:")
print(players[:3])

print("Three items from the middle of the list are:")


print(players[int(len(players)/2)-1:int(len(players)/2)+2])
print(players[-3:])

