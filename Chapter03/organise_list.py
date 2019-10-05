# the type must be same to order
cars = ['bmw', 'audi', 'audi', 'toyota', 'subaru', '4']
print(cars)

cars[1] = cars[1].title()
cars.append("BMW")
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print(sorted(cars))
print("test -1 {}".format(cars))

print(f"test {sorted(cars,reverse=True)}")
print(cars)

cars.insert(-2,['table','disk'])
print(cars)

# print(sorted(cars))
# TypeError: '<' not supported between instances of 'list' and 'str

cars[-3].sort()
print(cars)

cars.reverse()
print(cars)

numeric = [4,5,67,8,-1,0,9,9.8,-34.6]

numeric.sort()
print(numeric)

print(len(numeric))

location = ['US','UK','AU','JP','HK']
print(location)
print(sorted(location))

a = sorted(location, reverse=True)
print(a)

print(location)

location.reverse()
print(location)

location.reverse()
print(location)

a.sort()
print(a)

a.sort(reverse=True)
print(a)

print(len(a))
print()

# one variable refer to another, when the refered variable change, \ 
# the refering one will be changed
compute = ['mouse','keyboard','monitor']
temp = compute
print(f"I think the compute is make of {compute}")
print(f"Maybe order by alphabetic, {sorted(compute)}")
print(f"Maybe order by reverse alphabetic, {sorted(compute,reverse=True)}")
temp.reverse()
print(f"The part I owned from the newest to the oldest, {temp}")
temp.reverse()
soul = 'host'
print("Maybe I forget the {}".format(soul))
compute.append(soul)
print(compute)
soul = 'host2'
print(temp)
temp.insert(len(temp)+1,soul)
print(f"test {temp}")
soul = 'host3'

temp.insert(-1,soul)
print(temp)

print(compute.pop())
print(temp)

print(compute.pop(-1))
print(temp)

print(compute.remove("host"))
print(temp)

del compute[len(temp)-1]
print(temp)

print("-------------")
b = print(temp)
print(b)

c = []
print(len(c))