"""
Author: Adeline Chew Yao Yi
ID: 31164110
"""


# ---------------------Task 1 Sorting Function-----------------------#


def get_digit(num, d):
    """[Get the value of the d-th digit of number]
    Complexity: 
        Time: O(1)
        Aux space: TODO
    Args:
        num ([int]): [integer input]
        d ([int]): [d-th digit]
    Returns:
        [int]: [single digit represents the d-th value]
    """
    base = 10
    res = (num // (base ** d) % base)
    return res


def swap(arr1, arr2):
    """[Copy all items from arr2 to arr1]
    Complexity:
        Time: O(N) where N is the length of arr1
        Aux space: TODO
    Args:
        arr1 ([List]): [New list for copy]
        arr2 ([List]): [List to be copied]
    Returns:
        arr1
    """
    for item in range(len(arr1)):
        arr1[item] = arr2[item]
    return arr1


def radix_sort_aux(arr, base, digit, length):  
    """[A counting sort that sort integers based on the d-th digit]
    Complexity: 
        Time: O(N) where N is the length of input array
        Space: TODO
    Args:
        arr ([List]): [Unsorted list]
        base ([Int]): [Base of the integers in list]
        digit ([Int]): [d-th digit for the integer to be sorted]
        length ([Bool]): [Length is used to indicate this function
                        is used to sort length of words]
    Returns:
        [List]: [Sorted array]
    """
    n = len(arr)
    counter_arr = [0] * base
    pos_arr = [1] + [0] * (base - 1)
    temp_arr = [1] + [0] * (n - 1)
    for i in range(n): # calculate the freq of items
        if length: 
            counter_arr[len(arr[i][0])] += 1
        else:
            counter_arr[get_digit(arr[i], digit)] += 1
    for v in range(1, base):
        pos_arr[v] = pos_arr[v - 1] + counter_arr[v - 1]
    for i in range(n):  # Place items according to index indicated in pos_arr
        if length:
            value = len(arr[i][0])
        else:
            value = get_digit(arr[i], digit)
        temp_arr[pos_arr[value] - 1] = arr[i]
        pos_arr[value] += 1
    arr = swap(arr, temp_arr)
    return arr


def radix_sort(arr, length=False):
    """[A LSD radix sort implementation]
    Complexity: 
        Time: O(NK) where N is the length of input and 
            K is the greatest number of digits in the items in the input list
        Space: TODO
    Args:
        arr ([List]): [Input unsorted list]
        length ([Bool]): [Indicate this function is used to sort length of words]. Defaults to False.
    Returns:
        [List]: [Sorted list]
    """
    max_num = 0
    digit = 0
    if length:
        arr = radix_sort_aux(arr, 10, 0, length)
    else:
        for i in arr:   # Get the maximum number in list
            if max_num < i:
                max_num = i
        while max_num != 0: # Get the number of digits for maximum number
            max_num = max_num // 10
            digit += 1
        for d in range(0, digit):   
            arr = radix_sort_aux(arr, 10, d, length)
    return arr


# ---------------------Best Interval-----------------------#


def best_interval(transactions, t):
    """[A function that finds the maximum elements for a particular time interval]
    Complexity: 
        Time: O(NK) where N is the length of transactions
            and K is the greatest number of digits in elements
            in the transactions list
        Space: TODO
    Args:
        transactions ([List]): [Unsorted non-negative integer list]
        t ([Int]): [A length of time]
    Returns:
        [Tuple]: [(The time that the best interval started, Total elements in the interval)]
    """
    n = len(transactions)
    max_count = 0
    max_count_index = 0

    transactions = radix_sort(transactions)
    j = 0
    for i in range(n):
        # end point (Interval starting at j and ending at j + t)
        k = transactions[j] + t  
        if transactions[i] <= k:
            if i - j + 1 > max_count:   # Elements between i and j > max
                max_count = i - j + 1
                max_count_index = max(transactions[i] - t, 0)   # started time
        else:
            j += 1
    return max_count_index, max_count


# ---------------------Sorting functions for Task 2-----------------------#


def get_char(word, d):
    """[Get the ASCII value of characters and minus 97 (So 'a' will be 0)]
    Complexity: 
        Time: O(1), ord() takes O(1) complexity
        Space: TODO
    Args:
        word ([String]): [Input word]
        d ([Int]): [To get d-th digit character]
    Returns:
        [type]: [description]
    """
    if d < len(word):
        return ord(word[d]) - 97
    return -1


def radix_sort_str(arr): 
    """[summary]

    Args:
        arr ([type]): [description]

    Returns:
        [type]: [description]
    """
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


def counting_sort_letter(word):  # sort word to anagram
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
    return res, word


def words_with_anagrams(list1, list2):
    new_lst1, new_lst2 = [], []
    res = []
    first = 0
    sec = 0
    for i in range(len(list1)):  # take O(nm) n = len(list) and m = length of longest word
        new_lst1.append(counting_sort_letter(list1[i]))
    for i in range(len(list2)):
        new_lst2.append(counting_sort_letter(list2[i]))
    new_lst1 = radix_sort_str(radix_sort(new_lst1, True))
    new_lst2 = radix_sort_str(radix_sort(new_lst2, True))
    print("List 1: " + str(new_lst1))
    print("List 2: " + str(new_lst2))

    while first < len(new_lst1) and sec < len(new_lst2):
        word1, word2 = new_lst1[first][0], new_lst2[sec][0]
        if new_lst1[first][0] == new_lst2[sec][0]:
            res.extend(new_lst1[first][1])
            first += 1
            sec += 1
        elif len(word1) == len(word2):
            i, j = 0, 0
            while i < len(word1) and i < len(word2):
                if ord(word1[i]) > ord(word2[j]):
                    sec += 1
                    break
                elif ord(word2[j]) > ord(word1[i]):
                    first += 1
                    break
                else:
                    i += 1
                    j += 1
        elif len(word1) > len(word2):
            sec += 1
        else:
            first += 1
    return res


# ---------------------Test Cases-----------------------#
t = 5
transactions = [11, 1, 3, 1, 4, 10, 5, 7, 10]
t1 = 3
transactions1 = [2, 4, 4, 4, 6, 10]
lst1 = ["spot", "tops", "dad", "simple", "dine", "cats"]
lst2 = ["pots", "add", "simple", "dined", "acts", "cast"]
lst3 = ["aaaa", "aab", "ba", "aac", "bab", "aa"]
lst4 = ["aaa", "aba", "bba", "abb", "a", "c"]
# print(best_interval(transactions, t))
# print(radix_sort_str(lst1))
# print(words_with_anagrams(lst1, lst2))
# print(best_interval([1, 2, 4, 4, 4, 6, 10], 1)) # (3, 3)
# print(best_interval([11,1,1,11,1,1,1,1, 2, 4, 4, 4, 7, 10], 5)) # (0, 10)
# print(best_interval([15,17,20,21,22,22,24,26,29,30,31], 5)) # (17, 5)
# print(best_interval([15,21,22,22,24,25,29,30,31], 5)) # (20, 5)
# print(best_interval([5,1,5,1,5,1,5,1,5,1,5,1], 1)) # (0, 6)
# print(best_interval([3, 2, 3], 5)) # (0, 3)
# print(best_interval([85, 106, 152, 153, 284, 297, 310, 348, 391, 425, 506, 572, 578, 666, 671, 711, 727, 755, 758, 852, 908, 961], 100)) # (658, 6)

## Test cases from Ed
print(best_interval([1, 5, 6], 5) == (1, 3))  # (0 - 5) contains 2 items but (1 - 6) contains 3 items, #(1, 3)
print(best_interval([1, 5, 5], 5) == (0, 3))  # (0 - 5) contains 3 items #(0, 3)
print(best_interval([1, 5], 5) == (0, 2))  # (0 - 5) contains 2 items # (0, 2)
print(best_interval([1], 5) == (0, 1))  # (0 - 1) contains 1 items # (0, 1)
print(best_interval([1], 1) == (0, 1))  # (0 - 1) contains 1 items # (0, 1)
print(best_interval([1, 2, 3, 4, 5, 6, 7], 0) == (1, 1))    # (1, 1)
print(best_interval([11, 1, 3, 1, 4, 10, 5, 7, 10], 5) == (0, 5))   # (0, 5)
print(best_interval([11, 1, 3, 1, 4, 10, 5, 7, 10], 6) == (1, 6))   # (1, 6)
print(best_interval([], 6) == (0, 0))   # (0, 0)
print(best_interval([0], 2) == (0, 1))  # (0, 1)
print(best_interval([0], 1) == (0, 1))  # (0, 1)
print(best_interval([0], 4) == (0, 1))  # (0, 1)
print(best_interval([0, 2, 3], 4) == (0, 3))    # (0, 3)
print(best_interval([0, 2, 3], 0) == (0, 1))    # (0, 1)
print(best_interval([0], 0) == (0, 1))  # (0, 1)
print(best_interval([1], 1) == (0, 1))  # (0, 1)
print(best_interval([0], 1) == (0, 1))  # (0, 1)
print(best_interval([0, 0, 0, 0, 0], 1) == (0, 5))  # (0, 5)
print(best_interval([11, 1, 3, 1, 4, 10, 5, 7, 10, 11, 11, 11, 12, 11, 11, 11, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 16], 5)==(10,21)) # (10, 21)
print(best_interval([11, 1, 3, 1, 4, 10, 5, 7, 10],11)==(0,9))  # (0, 9)
print(best_interval([1,1,1,1,1,1,1,1], 0) == (1, 8))    # (1, 8)
print(best_interval([1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2], 0) == (2, 10))   # (2, 10)
print(best_interval([11,11,11,11,11,11,10,10,5], 2) == (9,8))
print(best_interval([9,9,9,9,9,9,9,9,10,10], 6) == (4, 10))
print(best_interval([11, 1, 3, 1, 4, 10, 5, 7, 10], 11) == (0, 9))
print(best_interval([11, 1, 3, 1, 4, 10, 5, 7, 10], 0) == (1,2))

# ---------------------Anagram Test Cases-----------------------#
        