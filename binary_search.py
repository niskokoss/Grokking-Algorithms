import math
list1 = list(range(0, 10000 + 1, 2))
item = 2200


def binary_search(list, item):
    check = 0
    low = 0
    high = len(list) - 1

    while low <= high:
        check += 1
        mid = math.floor((low + high) / 2)
        x = list[mid]
        if x == item:
            return mid
        if x > item:
            high = mid - 1
        else:
            low = mid + 1


print(binary_search(list1, item))
