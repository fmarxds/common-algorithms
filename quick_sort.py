def qsort(arr: list):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) // 2]
    lowers = []
    highers = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            lowers.append(arr[i])
        else:
            highers.append(arr[i])
    return qsort(lowers) + [pivot] + qsort(highers)


if __name__ == '__main__':
    arr = [1, 3, 2, 6, 4, 5, 1]
    print(qsort(arr))
