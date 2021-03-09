from bigO import BigO
import random

"""
Rmb to undo the commented isSorted in 
/Users/adelinechew/Library/Python/3.7/lib/python/site-packages/bigO/BigO.py
line 418
"""

t = 5
transactions = [11, 1, 3, 1, 4, 10, 5, 7, 10]
t1 = random.randint(0, 100000)
transactions1 = [102, 1048, 294, 2, 302, 302, 3283, 302, 2, 4082, 44444, 10293, 4, 7, 56, 3495]
ls = res = random.sample(range(1, 2000000), random.randint(0, 10000))

def swap(arr1, arr2):
    for item in range(len(arr1)):
        arr1[item] = arr2[item]
    return arr1


def counting_sort(arr):  # example in notes
    """[
        Best : O(n) Time
        Average : O(n) Time
        Worst : O(nlog(n)) Time
    ]
    Args:
        arr ([type]): [description]

    Returns:
        [type]: [description]
    """
    for i in range(len(arr)):
        arr[i] = abs(arr[i])
    # print(arr)
    n = len(arr)
    u = max(arr)
    # print("Max (u) = " + str(u))
    # print("Length of n - 1 = " + str(n))
    counter_arr = [0] * u
    # print("Length of counter_arr: " + str(len(counter_arr)))
    pos_arr = [1] + [0] * (u - 1)
    temp_arr = [1] + [0] * (n - 1)
    i = 1
    try:
        for i in range(n):
            counter_arr[arr[i] - 1] += 1
    except IndexError:
        print("i = " + str(i))
    for v in range(1, len(counter_arr)):
        pos_arr[v] = pos_arr[v - 1] + counter_arr[v - 1]
    for i in range(n):
        temp_arr[pos_arr[arr[i] - 1] - 1] = arr[i]
        pos_arr[arr[i] - 1] += 1
    arr = swap(arr, temp_arr)
    return arr


def get_digit(num, base, d):  # Currently work for base 10 only
    exp = base ** d
    division = base ** (d - 1)
    num %= exp
    res = (num // division) * division
    return res


def radix_pass(arr, b, digit):
    counter_ls = [0] * b
    pos_ls = [1] * [0] * (b - 1)
    n = len(arr)
    for i in range(1, n):
        counter_ls[get_digit(arr[i], b, digit)] += 1
    # for v in range(1, b - 1):
    #     pos_ls


def radix_sort(arr, b, digits):
    for d in range(1, digits):
        radix_pass(arr, b, d)


def best_interval(transactions, t):
    max_count = 0
    max_count_index = 0
    length = len(transactions)
    max_num = max(transactions)  # O(n)
    new_trans_ls = counting_sort(transactions, max_num)  # sorted list
    reversed_ls = new_trans_ls[::-1]  # O(n) descending list
    j = 0
    k = new_trans_ls[j] + t  # end point
    # print(reversed_ls)
    for i in range(length):
        if 0 < i < length - 1 and reversed_ls[i] >= k >= reversed_ls[
            i + 1]:  # if reach the endpoint, calculate length between both endpoint
            print("i: " + str(i) + " j: " + str(j))
            reversed_index = length - i - 1
            if reversed_index - j >= max_count:
                max_count = reversed_index - j
                max_count_index = new_trans_ls[j]
            j += 1
            k = new_trans_ls[j] + t
    return (max_count_index, max_count)
    # print(new_endpt_ls)


lib = BigO()
complexity = lib.test_all(counting_sort)
arr = lib.genRandomArray(50)
# print(arr)
# print(counting_sort1(arr))

# print(best_interval(ls, t1))
# print(counting_sort2([102, 1048, 294, 2, 403, 3283, 4082, 44444, 10293, 4, 7, 56, 3495]))
