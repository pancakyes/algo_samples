#selection sort sample. O(n**2)

#case 1 with creating new list/array
def find_min_1(arr):
    the_min = arr[0]
    for item in arr:
        if the_min > item:
            the_min = item
    return the_min

def selection_sort_1(arr):
    sorted_arr = []
    for _ in range(len(arr)):
        the_min = find_min_1(arr)
        sorted_arr.append(the_min)
        arr.remove(the_min)
    return sorted_arr

#tests
print(selection_sort_1([2,4,1,5,7]))
print(selection_sort_1([1,1,1]))

#case 2 with reordering list/array
def find_min_2(arr, ind):
    index_min = ind
    for current_index in range(ind,len(arr)):
        if arr[index_min] > arr[current_index]:
            index_min = current_index
    return index_min

def selection_sort_2(arr):
    for ind in range(len(arr)):
        index_min = find_min_2(arr, ind)
        temp_value = arr[ind]
        arr[ind] = arr[index_min]
        arr[index_min] = temp_value
    return arr

#some tests
print(selection_sort_2([2,4,1,5,7]))
print(selection_sort_2([1,1,1]))
