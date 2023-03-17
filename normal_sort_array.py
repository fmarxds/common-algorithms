def reverse(coll: list):
    reversed_coll = []
    for i in range(len(coll) - 1, -1, -1):
        reversed_coll.append(coll[i])
    return reversed_coll


def sort(coll: list):
    items = coll.copy()
    sorted_coll = []
    while len(items) > 0:
        selected_item = 0
        selected_item_idx = 0
        for i in range(0, len(items)):
            if selected_item <= items[i]:
                selected_item_idx = i
                selected_item = items[i]
        sorted_coll.append(items.pop(selected_item_idx))
    return reverse(sorted_coll)


if __name__ == '__main__':
    print(sort([3, 4, 1, 5, 2, 2, 3]))

