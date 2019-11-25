"""A class represent the lottery"""

from random import choice

class Lottery():
    """model lottery"""

    def __init__(self):
        """initialize the lottery"""
        self.element_list = ('0','1','2','3','4','5','6','7',
                            '8','9','a','b','c','d','e')
    
    def prize_number(self):
        """generate the prize number"""
        return [choice(self.element_list),choice(self.element_list),
            choice(self.element_list),choice(self.element_list)]

