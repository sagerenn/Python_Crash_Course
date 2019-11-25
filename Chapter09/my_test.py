import restaurant_class as rest

my_retaurant = rest.Restaurant('sdf','dgrth')
my_retaurant.describe_restaurant()

from admin_class import Admin

my_admin = Admin('ss','zz',location='gz')
my_admin.show_privileges()

from dice import Dice

six_dice = Dice()
for i in range(0,10):
    print(six_dice.roll_dice(), sep=' ', end=' ')

print()

ten_dice = Dice(10)
for i in range(0,10):
    print(ten_dice.roll_dice(), sep=' ', end=' ')

print()

twenty_dice = Dice(20)
for i in range(0,10):
    print(twenty_dice.roll_dice(), sep=' ', end=' ')

print()

import lottery

my_lottry = lottery.Lottery()
prize_num = my_lottry.prize_number()

my_ticket = ['4','7','b','2']

for i in range(1,100000000):
    prize_num = my_lottry.prize_number()
    if my_ticket == prize_num:
        print(f'maybe after {i} times, you will win the price, {prize_num}')
        break

if my_ticket != prize_num:
    print('hard to win!!!')
