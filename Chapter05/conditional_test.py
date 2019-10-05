registered_users = ['admin','test','user']

if registered_users:
    for user in registered_users:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")

print("--------------------")

registered_users = []

if registered_users:
    for user in registered_users:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("we need to find some users!")

registered_users = ['Admin','Test','user']
temp_users = []

for user in registered_users:
    temp_users.append(user.lower())

print(temp_users)

new_users = ['test','root']
for new_user in new_users:
    if new_user in temp_users:
        print(f"The {new_user} is used!")
    else:
        print(f"The {new_user} is avaiable!")


num_lists = [1,2,3,4,5,6,7,8,9,65]
for num in num_lists:
    if num % 10 == 1:
        print(f"{num}st")
    elif num % 10 == 2:
        print(f"{num}nd")
    elif num % 10 == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")
