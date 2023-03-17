import time
from datetime import datetime


def regular_search_item_idx(coll, item):
    for i in range(0, len(coll)):
        if coll[i] == item:
            return i
    return None


def search_item_idx(coll, item):
    low = 0
    high = len(coll)
    while low < high:
        medium = (low + high) // 2
        maybe_item = coll[medium]
        if maybe_item == item:
            return medium
        if maybe_item > item:
            high = medium - 1
        else:
            low = medium + 1
    return -1


def search_item_idx_recursive(arr, low, high, find):

    if low >= high:
        return -1

    mid = (low + high) // 2
    maybe = arr[mid]

    if find == maybe:
        return mid

    elif find < maybe:
        return search_item_idx_recursive(arr, low, mid - 1, find)

    else:
        return search_item_idx_recursive(arr, mid + 1, high, find)


if __name__ == "__main__":

    coll = range(100000000)
    item = 99999999

    start = datetime.now()
    item_idx = search_item_idx(coll, item)
    stop = datetime.now()
    print('### Binary Search')
    print(f'Index of item {item}: {item_idx}')
    print(f'Elapsed time: {stop - start}')

    print()

    start = datetime.now()
    item_idx = regular_search_item_idx(coll, item)
    stop = datetime.now()
    print('### Regular Search')
    print(f'Index of item {item}: {item_idx}')
    print(f'Elapsed time: {stop - start}')

    print()

    start = datetime.now()
    item_idx = search_item_idx_recursive(coll, 0, len(coll), item)
    stop = datetime.now()
    print('### Recursive Binary Search')
    print(f'Index of item {item}: {item_idx}')
    print(f'Elapsed time: {stop - start}')
