num_lists = [34,678,234,5,76,34,-234,6454,4,6,56,88,345,567,8,923,56]

# the counter records the closest larger number with the pivot and exchange 
# with the pivot in the ends
def partition(array,start,end):
    pivot = end
    loop = counter = start
    while loop < end:
        if array[loop] <= array[pivot]:
            array[counter], array[loop] = array[loop], array[counter]
            counter += 1
        loop += 1
    array[counter], array[pivot] = array[pivot], array[counter]
    return counter

# the counter records the closest larger number with the pivot and exchange 
# with the pivot in the ends
def _partition(array,start,end):
    pivot = start
    loop = counter = start
    mark = 0
    while loop <= end: 
        if array[loop] < array[pivot] and mark != 0:
            counter += 1
            array[counter], array[loop] = array[loop], array[counter]                                                                             
        elif array[loop] < array[pivot]:
            counter += 1
        elif array[loop] > array[pivot]:
            mark += 1
        loop += 1
    array[counter], array[pivot] = array[pivot], array[counter]
    return counter

def qsort(array,start,end):
    if start < end:
        p = partition(array,start,end)
        qsort(array,start,p-1)
        qsort(array,p+1,end)
    else:
        return

def quicksort(array):
    qsort(array,0,len(array)-1)

quicksort(num_lists)
print(num_lists)
