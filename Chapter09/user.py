class User:
    """Simulate a user"""

    def __init__(self, first_name, last_name, **user_info):
        """pass the dictionary of user info to class"""
        self.user_info = user_info
        self.user_info['first_name'] = first_name
        self.user_info['last_name'] = last_name
        self.user_info['login_attempts'] = 0

    def describe_user(self):
        """print all info of user"""
        print(self.user_info)

    def greet_user(self):
        """print a personalized greeting"""
        print(f"haha {self.user_info}")

    def increment_login_attempts(self):
        """increase one to the login attempts"""
        self.user_info['login_attempts'] += 1

    def reset_login_attempts(self):
        """reset the number of login attempts"""
        self.user_info['login_attempts'] = 0

# susan_zeng_info = {
#     'first_name': 'susan', 
#     'last_name': 'zeng', 
#     'location': 'guagnzhou',
#     }

susan_zeng = User('susan','zeng', location='guangzhou')
susan_zeng.describe_user()
susan_zeng.user_info['first_name'] = 'joanna'
susan_zeng.greet_user()
susan_zeng.increment_login_attempts()
susan_zeng.increment_login_attempts()
print(susan_zeng.user_info)
susan_zeng.reset_login_attempts()
print(susan_zeng.user_info)



class Admin(User):
    """model a admin user from the user class"""

    def __init__(self, first_name, last_name, **user_info):
        """initialize the admin user"""
        # tmp_string = ''
        # count = 0
        # for k,v in user_info.items():
        #     count += 1
        #     if count == 1:
        #         tmp_string += f"{k} = '{v}'"
        #     else:
        #         tmp_string += f", {k} = '{v}'"
        super().__init__(first_name, last_name, **user_info)
        self.privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges_b = \
            Privileges(["can add post", "can delete post", "can ban user"])

    def show_privileges(self):
        print(self.privileges)
        print(self.__dict__)



class Privileges():
    """model the privileges of users"""

    def __init__(self, list_action):
        """initialize the privileges"""
        self.privileges = list_action

    def show_privileges(self):
        print(self.privileges)

susan = Admin('susan','zeng',location='ggzhou',company='m')
susan.show_privileges()
print(susan.user_info)
print(susan)


joanna = Admin('joanna','zhang',location='hkou',company='li')
joanna.privileges_b.show_privileges()
print(joanna.privileges_b.__dict__)