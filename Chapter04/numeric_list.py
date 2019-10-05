for value in range(1,5):
    print(value)

# 1
# 2
# 3
# 4

for value in range(3):
    print(value)

num_list = list(range(9))
print(num_list)

tmp = list(num_list)
tmp2 = num_list
tmp.append(8)
num_list.append(10)
print(tmp,num_list,tmp2)

even_numbers = list(range(2,11,2))
print(even_numbers)


even_numbers = list(range(2,10,2))
print(even_numbers)

squares = list()
for value in range(1,11):
    squares.append(value ** 2)

print(squares)

num_statistic = list(range(3,200,7))
print(len(num_statistic),min(num_statistic),max(num_statistic), \
    sum(num_statistic),num_statistic)

# >>> a = [ value for value in range(1,5) ] 
# >>> print(a)
# [1, 2, 3, 4]
# >>> 

squares = [ value ** 2 for value in range(3,70,7) ]
print(squares)

for value in range(1,21):
    print(value,sep="",end=" ")

print()
million_num_list = [ value for value in range(1,10**6+1) ]
print(len(million_num_list),min(million_num_list),max(million_num_list), \
    sum(million_num_list))
# for value in range(10**9):
#     print(value)


for value in range(1,20,2):
    print(value,sep="",end=" ")
print()


for value in range(3,30+1):
    print(value ** 3,sep="",end=" ")
print()

cubes = [value ** 3 for value in range(1,10+1)]
print(cubes)

