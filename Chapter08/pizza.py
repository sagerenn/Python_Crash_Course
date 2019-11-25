from make_pizza import mk_pizza # similar the source in shell 

mk_pizza(16,"mushroom","pineapple")
mk_pizza(12,"meat","tor")


import make_pizza # similar the source in shell 

make_pizza.mk_pizza(16,"mushroom","pineapple")
make_pizza.mk_pizza(12,"meat","tor")


from make_pizza import mk_pizza as mp

def mk_pizza(size,*toppings):
    print(size,toppings)

mk_pizza(16,"mushroom","pineapple")
mk_pizza(12,"meat","tor")
mp(12,"meat","tor")

import make_pizza as p

p.mk_pizza(16,"mushroom","pineapple")

from make_pizza import *

mk_pizza(12,"meat","tor")


def test(
        arg1,arg2,
        arg3='dsf',arg4='sdf'):
    print(arg1,arg2,arg3,arg4)

test('sd','sdfg')