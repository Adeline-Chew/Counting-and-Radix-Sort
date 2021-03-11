import string
import random


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


print(radix_sort(["spot", "tops", "dad", "simple", "dine", "cats"]))
print(radix_sort(["pots", "add", "simple", "dined", "acts", "cast"]))

letter = string.ascii_lowercase
ls = []
for i in range(100):
    ls.append(''.join(random.choice(letter) for i in range(10)))
print(ls)
print(radix_sort(ls))

#%%

# %%
