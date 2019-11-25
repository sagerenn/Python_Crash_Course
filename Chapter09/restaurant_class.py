"""A class that can be used to represent a restaurant."""

class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """describe the restaurant infomation"""
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The cuisine type provided by restaurant is {self.cuisine_type}")

    def open_restaurant(self):
        """state the status of restaurant"""
        print("The restaurant is open.")

    def get_number_served(self):
        """get the number served"""
        print(self.number_served)

    def set_number_served(self, number_served):
        """set the number of customer"""
        if self.number_served < number_served:
            self.number_served = number_served

    def increment_number_served(self, number_increment):
        """the number to add"""
        self.number_served += number_increment
