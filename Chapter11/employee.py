"""A class present employee"""

class Employee:
    """model the info of employee"""

    def __init__(self, first, last, salary):
        """initialize the info of employee"""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, add_salary=5000):
        """increase the annual salary"""
        self.salary += add_salary
