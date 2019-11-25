sandwich_orders = ['Doner Sandwich', 'pastrami', 'Reuben Sandwich', 
                    'pastrami', 'Shawarma Sandwich',
                    'pastrami','pastrami']
finished_sandwiches = []


if 'pastrami' in sandwich_orders:
    print(f"All of The pastrami have been run out, please change the order!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

count = 0

while sandwich_orders:
    count += 1
    sandwich_made = sandwich_orders.pop(0)
    if sandwich_made != 'pastrami':
        print(f"The {count} {sandwich_made} is made!")
        finished_sandwiches.append(sandwich_made)
    else:
        print(f"The pastrami of {count} has been run out")

# print(sandwich_orders[0])

print(f"The all sandwich({finished_sandwiches}) is made!")

flag = 1
user_vacation = {}
while flag == 1:
    username = input("What's your name? ")
    vacation = input("Where is your dream vacation? ")
    user_vacation[username] = vacation
    if input("Any other people?(yes/no)") == 'no':
        flag = 0

for user, vac in user_vacation.items():
    print(f"{user}'s dream vacation is {vac}")
