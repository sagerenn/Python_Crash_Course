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

top_restaurant = Restaurant('xianggelila','zizhu')
print(top_restaurant.restaurant_name,top_restaurant.cuisine_type)
top_restaurant.describe_restaurant()
top_restaurant.open_restaurant()

su_restaurant = Restaurant('suba','haha')
jj_restaurant = Restaurant('jingxiang','chuachua')
su_restaurant.describe_restaurant()
jj_restaurant.describe_restaurant()

num_restaurant = Restaurant('sdf','dfg')
num_restaurant.get_number_served()
num_restaurant.number_served = 9
num_restaurant.get_number_served()

num_restaurant.set_number_served(10)
num_restaurant.get_number_served()

num_restaurant.increment_number_served(10)
num_restaurant.get_number_served()


class IceCreamStand(Restaurant):
    """a specific kind of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize the instance of ice cream stand
        state the flavor list supported
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavor_list = ["Cookies and Cream.", "Chocolate Ice Cream.", 
                "Vanilla Ice Cream.", "Chocolate Chip.", "French Vanilla.", 
                "Strawberry.", "Peanut Butter Cup.", "Rocky Road."]

    def list_all_flavor(self):
        """list all flavor in the ice cream stand"""
        for flavor in self.flavor_list:
            print(flavor)

one_ice_cream = IceCreamStand('sdf','dfg')
one_ice_cream.list_all_flavor()