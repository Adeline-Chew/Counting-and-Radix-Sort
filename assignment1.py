# from bigO import BigO
import random
import binascii

"""
Rmb to undo the commented isSorted in 
/Users/adelinechew/Library/Python/3.7/lib/python/site-packages/bigO/BigO.py
line 418
"""

t = 5
transactions = [11, 1, 3, 1, 4, 10, 5, 7, 10]
t1 = random.randint(0, 100000)
transactions1 = [102, 1048, 294, 2, 302, 302, 3283,
                 302, 2, 4082, 44444, 10293, 4, 7, 56, 3495]
ls = res = random.sample(range(1, 2000000), random.randint(0, 10000))


def swap(arr1, arr2):
    for item in range(len(arr2)):
        arr1[item] = arr2[item]
    return arr1


def counting_sort(arr, index=False):  # example in notes
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
    n = len(arr)
    u = max(arr)
    counter_arr = [0] * u
    pos_arr = [1] + [0] * (u - 1)
    temp_arr = [1] + [0] * (n - 1)
    i = 1
    index_ls = [0] * n
    try:
        for i in range(n):
            counter_arr[arr[i] - 1] += 1
    except IndexError:
        print("i = " + str(i))
    for v in range(1, len(counter_arr)):
        pos_arr[v] = pos_arr[v - 1] + counter_arr[v - 1]
    for i in range(n):
        temp_arr[pos_arr[arr[i] - 1] - 1] = arr[i]
        res[i] = pos_arr[arr[i] - 1] - 1 # index list for anagram
        pos_arr[arr[i] - 1] += 1
    arr = swap(arr, temp_arr)
    if index:
        return (res, arr)
    return arr

# %%


def get_digit(num, base, d):  # Currently work for base 10 only
    res = int((num // (base ** (d)) % base))
    return res


# print(get_digit(1042, 10,  3))


def counting_sort_aux(arr, base, digit):  # example in notes
    n = len(arr)
    counter_arr = [0] * base
    pos_arr = [1] + [0] * (base - 1)
    temp_arr = [1] + [0] * (n - 1)
    i = 1
    for i in range(n):
        counter_arr[get_digit(arr[i], base, digit)] += 1
    for v in range(1, base):
        pos_arr[v] = pos_arr[v - 1] + counter_arr[v - 1]
    for i in range(n):
        digit1 = get_digit(arr[i], base, digit)
        temp_arr[pos_arr[digit1] - 1] = arr[i]
        pos_arr[digit1] += 1
    arr = swap(arr, temp_arr)
    return arr


def radix_sort(arr, b, digits, to_int=False): 
    if to_int:
        for i in range(len(arr)):
            arr[i] = ord(arr[i]) - 97
    for d in range(0, digits):
        arr = counting_sort_aux(arr, b, d)
    if to_int:
        for i in range(len(arr)):
            arr[i] = chr(arr[i] + 97)
    return arr
# print(radix_sort([102, 1048, 294, 2, 403, 3283, 4082, 44444, 10293, 4, 7, 56, 3495], 10, 5))


def best_interval(transactions, t):
    max_count = 0
    max_count_index = 0
    length = len(transactions)
    max_num = max(transactions)  # O(n)
    # sorted list, try to change it into radix sort
    new_trans_ls = counting_sort(transactions, max_num)
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


# lib = BigO()
# complexity = lib.test_all(counting_sort)
# arr = lib.genRandomArray(50)
# print(arr)
# print(counting_sort1(arr))

# print(best_interval(ls, t1))
# print(counting_sort2([102, 1048, 294, 2, 403, 3283, 4082, 44444, 10293, 4, 7, 56, 3495]))

# %%



def get_char(word, d):
    if d < len(word):
        return ord(word[d]) - 97
    return -1


def radix_sort_aux(arr, aux, lo, hi, d): # determine complexity
    radix = 26
    if hi <= lo:
        return
    count_ls = [0] * (radix + 2)  # 26 char + 2 blank
    for i in range(lo, hi + 1):
        count_ls[get_char(arr[i], d) + 2] += 1
    for r in range(radix + 1):
        count_ls[r + 1] += count_ls[r]
    for i in range(lo, hi + 1):
        char = get_char(arr[i], d) + 1
        count_ls[char] += 1
        count = count_ls[char]
        aux[count - 1] = arr[i]
        # aux[count_ls[get_char(arr[i], d) + 1] + 1] = arr[i]
    # print("Aux after counting: " + str(aux))
    for i in range(lo, hi + 1):
        arr[i] = aux[i - lo]
    for r in range(radix):
        radix_sort_aux(
            arr, aux, lo + count_ls[r], lo + count_ls[r + 1] - 1, d + 1)


def radix_sort(arr):  # without insertion sort
    n = len(arr)
    aux = [0] * n
    radix_sort_aux(arr, aux, 0, n - 1, 0)
    return arr


def convert_ls(lst): 
    res = []
    for word in lst:
        total = 0
        for i in range(len(word)):
            total += ord(word[i]) # check the complexity of accessing index 
        res.append(total)
    return res


def words_with_anagrams(list1, list2):
    n = len(list1)
    new_lst1 = radix_sort(list1)
    new_lst2 = radix_sort(list2)
    sum_lst1, sum_lst2 = convert_ls(new_lst1), convert_ls(new_lst2)
    tup1, tup2 = counting_sort(sum_lst1, True), counting_sort(sum_lst2, True)
    index1, sorted1 = tup1[0], tup1[1]
    index2, sorted2 = tup2[0], tup2[1]
    print("Sorted 1 = " + str(sorted1))
    print("Sorted 2 = " + str(sorted2))
    j = 0
    res = []
    for i in range(n):
        if sorted1[i] == sorted2[j]:
            res.append(new_lst1[index1[i]])
        if i > sorted2[j]:
            j += 1  
    return res


lst1 = ["spot", "tops", "dad", "simple", "dine", "cats"]
lst2 = ["pots", "add", "simple", "dined", "acts", "cast"]
print(words_with_anagrams(lst1, lst2))

# %%
# %%
