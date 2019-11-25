unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
denied_users = ['brian']

# for unconfirmed_user in unconfirmed_users:
#     if unconfirmed_user not in denied_users:
#         confirmed_users.append(unconfirmed_user)

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    if current_user not in denied_users:
        confirmed_users.append(current_user)

for confirmed_user in confirmed_users:
    print(f"The user f{confirmed_user} is confirmed!")


pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']

for pet in pets:
    if pet == "cat":
        pets.remove(pet)
        print(pets)

while 'cat' in pets:
    pets.remove(pet)

print(pets)

user_response = {}

while True:
    username = input("What's name? ").lower()
    response = input(f"Hi {username.title()}, where are you from? ")
    condition = input(f"Next? ")
    user_response[username] = response
    if condition.lower() == 'no':
        break

for user,result in user_response.items():
    print(f"{user} is from {result}")

