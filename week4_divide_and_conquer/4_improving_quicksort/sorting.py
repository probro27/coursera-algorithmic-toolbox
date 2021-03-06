# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    x = a[l]
    j = l # a[index] < x
    k = r # a[index] == x
    ## [2, 1, 2, 3, 4]
    for i in range(l, r + 1):
        if a[i] < x:
            a[i], a[j] = a[j], a[i]
            j += 1
            # [2, 1, 2, 3, 4]
    for i in range(r, l - 1, -1):
        if a[i] > x:
            a[i], a[k] = a[k], a[i]
            k -= 1
    
    for i in range(j, k):
        a[i], a[k] = a[k], a[i]
    # [1, 2, 2, 3, 4]
    return j, k 

def partition2(a, l, r):
    x = a[l]
    j = l
    ## [2, 1, 2, 3, 4]
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    # print(f"k = {k} for l = {l} and r = {r}")
    a[l], a[k] = a[k], a[l]
    #use partition3
    m,n = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, n, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # print(partition3(a, 0, n - 1))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
