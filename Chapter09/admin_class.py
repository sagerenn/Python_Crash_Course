"""a module represent an admin user"""

from user_class import User

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

