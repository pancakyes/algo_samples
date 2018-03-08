#binary search sample
def bin_search(arr, item):

    left_border, right_border = 0, len(arr) - 1
    arr.sort()
    count = 0

    while left_border < right_border:
        median = (right_border + left_border) // 2
        if arr[median] < item:
            left_border = median
            count += 1
        elif arr[median] > item:
            right_border = median
            count += 1
        else:
            return median, count

    return None, count

#some tests
a = list(range(128))
item = 27
print (bin_search(a,item))

a = list(range(128))
item = -50
print (bin_search(a,item))
