from functools import reduce


def sum(numbers):
    return reduce(lambda number, acc: acc + number, numbers)


def bubbleSort(numbers):
    sorted_list = numbers.copy()
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j +
                                            1] = sorted_list[j+1], sorted_list[j]
    return sorted_list


def sum_lists(list1, list2):
    if len(list1) != len(list2):
        raise Exception("Same size is required to sum two lists")
    sum_list = []
    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])
    return sum_list


if __name__ == "__main__":
    numbers = [1, 4, 3, 5, 2]
    print(sum(numbers))
    print(numbers)
    print(sum_lists(numbers, numbers))
