list1 = list(range(1, 10001))
print(list1)
item = 8753


def binary_search(list, item):
    low = 0
    high = len(list) + 1
    while True:
        mid = int((low + high + 1) / 2)
        x = list1[mid]
        if x == item:
            return list1[mid]
        if x > item:
            high = x - 1
        else:
            low = x - 1


print(binary_search(list1, item))
