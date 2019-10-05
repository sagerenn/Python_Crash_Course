first_name = 'ada'
last_name = 'lovelace'
print(first_name,last_name)
full_name = first_name + last_name
print(full_name)

full_name = first_name + " " + last_name
print(full_name)

full_name = f"{first_name.title()} {last_name.upper()}"
print(full_name)

full_name = f'first_name {last_name.lower()}'
print(full_name)

print(f'{full_name}'.upper())

print("{}+{}".format(first_name,last_name))

print("sdf\t \
dsf\nsdf dfhg")


print("sdf\tdfgdsf\nsdf dfhg")

print(" sdf ".lstrip())
print(" sdf ".rstrip(),sep=' ',end="$\n")
print(" sdf ".rstrip().lstrip(),sep=' ',end="$\n")
print()

# >>> a=" df fr "
# >>> a
# ' df fr '
# >>> a.strip()
# 'df fr'
# >>> a.rstrip()
# ' df fr'
# >>> a.lstrip()
# 'df fr '
# >>> 
# >>> a = a.lstrip()
# >>> a
# 'df fr '
# >>> 
# print('She's a beautiful girl!')
print("She's a beautiful girl!")

