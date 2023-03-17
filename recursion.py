def regressive(num):
    print(num)
    if num <= 0:
        return
    regressive(num - 1)


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


def factorial_tail(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return factorial_tail(n - 1, accumulator * n)


def sum_array(arr: list):
    if len(arr) == 1:
        return arr[0]
    return arr.pop() + sum_array(arr)


def sum_array_tail(arr: list, acc=0):
    if len(arr) == 1:
        return arr[0] + acc
    return sum_array_tail(arr, acc + arr.pop())


def count_array(arr: list):
    if not arr:
        return 0
    return 1 + count_array(arr[1:])


def count_array_tail(arr: list, acc=0):
    if not arr:
        return 0 + acc
    return count_array_tail(arr[1:], acc + 1)


def biggest_num(arr: list, biggest=0):
    if len(arr) == 1:
        return biggest
    if biggest <= arr[0]:
        biggest = arr[0]
    return biggest_num(arr[1:], biggest)


if __name__ == '__main__':
    print(biggest_num([1, 2, 9, 3, 4, 5]))
