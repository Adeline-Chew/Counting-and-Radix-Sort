

# ---------------------Function 1-----------------------#


def get_digit(num, base, d):
    res = int((num // (base ** (d)) % base))
    return res


def swap(arr1, arr2):
    for item in range(len(arr1)):
        arr1[item] = arr2[item]
    return arr1


def radix_sort_aux(arr, base, digit):  # example in notes
    n = len(arr)
    counter_arr = [0] * base
    pos_arr = [1] + [0] * (base - 1)
    temp_arr = [1] + [0] * (n - 1)
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


def radix_sort(arr, b, digits):
    for d in range(0, digits):
        arr = radix_sort_aux(arr, b, d)
    return arr

# ---------------------Best Interval-----------------------#


def best_interval(transactions, t):
    n = len(transactions)
    max_count = 0
    max_count_index = 0

    # TODO: need to eliminate max digit
    transactions = radix_sort(transactions, 10, len(str(max(transactions))))
    print(transactions)
    reversed_ls = transactions[::-1]  # O(n) descending list
    j = 0
    k = transactions[j] + t  # end point
    for i in range(n):
        if 0 < i < n - 1 and reversed_ls[i] >= k >= reversed_ls[i + 1]:
            reversed_index = n - i - 1
            if reversed_index - j >= max_count:
                max_count = reversed_index - j
                max_count_index = reversed_ls[i + 1] - t
            j += 1
            k = transactions[j] + t
    return (max_count_index, max_count)

# ---------------------Function 3-----------------------#


def get_char(word, d):
    if d < len(word):
        return ord(word[d]) - 97
    return -1

# arr = [(anagram, original word)]


def radix_sort_str(arr):  # determine the complexity, this is not in place
    d = 0
    radix = 26
    lo, hi = 0, len(arr) - 1
    count_ls = [0] * (radix + 2)  # 26 char + 2 blank
    r = 0
    aux = [0] * len(arr)
    res_arr = []
    while lo < hi and r < radix:
        for i in range(lo, hi + 1):
            count_ls[get_char(arr[i][0], d) + 2] += 1
        for r in range(radix + 1):
            count_ls[r + 1] += count_ls[r]
        for i in range(lo, hi + 1):
            anagram_word = arr[i][0]
            count_ls[get_char(anagram_word, d) + 1] += 1
            count = count_ls[get_char(anagram_word, d) + 1]
            aux[count - 1] = arr[i]
        for i in range(lo, hi + 1):
            arr[i] = aux[i - lo]
        temp_lo = lo
        lo = lo + count_ls[r]
        hi = temp_lo + count_ls[r + 1] - 1
        d += 1
        r += 1
    for i in range(len(arr)):
        if i > 0 and arr[i][0] == arr[i - 1][0]:
            res_arr[-1][1].append(arr[i][1])
        else:
            res_arr.append((arr[i][0], [arr[i][1]]))
    return res_arr


# ---------------------Anagram-----------------------#

"""
Algorithms:
(i) Sort every word to anagram (using counting sort), store in 
(anagram, original word)
(ii) Sort again by key, same key grp the values into list
[(anagram, [list of original words])]
    
"""


def ord_self(alphabet):
    return ord(alphabet) - 96


def counting_sort_letter(word): # sort word to anagram
    n = len(word)
    radix = 26
    count_ls = [0] * radix
    pos_ls = [1] + [0] * (radix - 1)
    temp_arr = [1] + [0] * (n - 1)
    for i in range(n):
        count_ls[ord_self(word[i]) - 1] += 1
    for v in range(1, len(count_ls)):
        pos_ls[v] = pos_ls[v - 1] + count_ls[v - 1]
    for i in range(n):
        temp_arr[pos_ls[ord_self(word[i]) - 1] - 1] = word[i]
        pos_ls[ord_self(word[i]) - 1] += 1
    # takes O(n) where n is the total length of temp arr (len(word))
    res = ''.join(temp_arr)
    return (res, word)


# def search(arr, key):
#     n = len(arr)
#     lo, hi = 0, n
#     while lo < hi:
#         mid = (lo + hi) // 2
#         mid_word = arr[mid][0]
#         i = 0
#         if ord(key[0]) >= ord(mid_word[0]):
#             if len(key) >= len(mid_word):
#                 index = len(mid_word)
#                 while i < index and ord(key[i]) >= ord(mid_word[i])
#             lo = mid
#         else:
#             hi = mid
#     if len(arr) > 0 and arr[lo][0] == key:
#         return True
#     else:
#         return False


def words_with_anagrams(list1, list2):
    new_lst1, new_lst2 = [], []
    res = []
    index = 0
    for i in range(len(list1)):  # take O(nm) n = len(list) and m = length of longest word
        new_lst1.append(counting_sort_letter(list1[i]))
    for i in range(len(list2)): 
        new_lst2.append(counting_sort_letter(list2[i]))
    new_lst1 = radix_sort_str(new_lst1)
    new_lst2 = radix_sort_str(new_lst2)
    print("List 1: " + str(new_lst1))
    print("List 2: " + str(new_lst2))
    # for i in range(len(new_lst1)):
        
    return res


# ---------------------Test Cases-----------------------#
t = 5
transactions = [11, 1, 3, 1, 4, 10, 5, 7, 10]
t1 = 3
transactions1 = [2, 4, 4, 4, 6, 10]
lst1 = ["spot", "tops", "dad", "simple", "dine", "cats"]
lst2 = ["pots", "add", "simple", "dined", "acts", "cast"]
# print(best_interval(transactions, t))
# print(radix_sort_str(lst1))
print(words_with_anagrams(lst1, lst2))
# print(words_with_anagrams(lst1, lst2))
# print(best_interval( [15,21,22,22,24,25,29,30,31], 5))