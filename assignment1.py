import random

t = 5
transactions = [11, 1, 3, 1, 4, 10, 5, 7, 10]  
t1 = random.randint(0, 100000) 
transactions1 = [102, 1048, 294, 2, 302, 302, 3283, 302, 2, 4082, 44444, 10293, 4, 7, 56, 3495]
ls = res = random.sample(range(1, 2000000), random.randint(0, 10000))

def counting_sort(ls): # complexity = O(N + U)
    n = len(ls)
    count_ls = [0] * n
    pos_ls = [1] + [0] * (n - 1)
    res = [0] * n
    for num in ls:
        count_ls[num - 1] += 1
    for i in range(1, len(count_ls)):
        pos_ls[i] = pos_ls[i - 1] + count_ls[i - 1]
    for num in ls:
        res[pos_ls[num - 1] - 1] = num 
        pos_ls[num - 1] += 1
    return res
  
def radix_sort(ls): # complexity = O()
    max_num = max(ls)
    exp = 1
    while max_num / exp > 0:
        counting_sort(ls, exp)
        exp *= 10
  
def best_interval(transactions, t):
    max_count = 0
    max_count_index = 0
    length = len(transactions)
    max_num = max(transactions)  # O(n)
    # new_trans_ls = counting_sort(transactions, max_num) # sorted list
    reversed_ls = new_trans_ls[::-1] # O(n) decending list
    j = 0
    k = new_trans_ls[j] + t # end point
    # print(reversed_ls)
    for i in range(length):
        if 0 < i < length - 1 and reversed_ls[i] >= k >= reversed_ls[i + 1]: # if reach the endpoint, calculate length between both endpoint
            print("i: " + str(i) + " j: " + str(j))
            reversed_index = length - i - 1
            if reversed_index - j >= max_count:
                max_count = reversed_index - j
                max_count_index = new_trans_ls[j]
            j += 1
            k = new_trans_ls[j] + t
    return(max_count_index, max_count)
    # print(new_endpt_ls)
    
    

print(best_interval(ls, t1))
# print(counting_sort([102, 1048, 294, 2, 403, 3283, 4082, 44444, 10293, 4, 7, 56, 3495], 44444))

