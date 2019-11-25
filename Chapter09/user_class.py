"""a module represent an user"""

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

