# Uses python3
from sys import stdin

def calc_fib(n):
    if (n <= 1):
        return n

    fibn = 0
    fibn_1 = 1
    fibn_2 = 1

    for i in range(2, n + 1):
        fibn_2 = fibn_1 + fibn
        fibn = fibn_1
        fibn_1 = fibn_2
    
    return fibn_2

def findPeriod(n):
    previous = 0
    current = 1
    for i in range(0, n * n):
        previous, current = current, (previous + current) % n
        if previous == 0 and current == 1:
            return i + 1


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    period = findPeriod(m)
    mod = n % period
    res = calc_fib(mod) % m
    return res

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    return (get_fibonacci_huge_naive(n + 1, 10) * get_fibonacci_huge_naive(n, 10))  % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_naive(n))
