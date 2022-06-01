# Uses python3
import sys

dict = {}

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
    
    dict[n] = fibn_2
    return fibn_2

def findPeriod(n):
    previous = 0
    current = 1
    for i in range(0, n * n):
        previous, current = current, (previous + current) % n
        if previous == 0 and current == 1:
            return i + 1


def get_fibonacci_huge_naive(n, m, period):
    if n <= 1:
        return n

    # period = findPeriod(m)
    mod = n % period
    if mod in dict:
        res = dict[mod] % m
    else:
        res = calc_fib(mod) % m
    return res

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    _sum      = 0
    period = findPeriod(10)

    mod = n % period

    for i in range(mod + 1):
        _sum += get_fibonacci_huge_naive(i, 10, period)

    return _sum % 10


def fibonacci_partial_sum_naive(from_, to):
    
    if from_ == 0:
        return fibonacci_sum_naive(to) % 10

    to_sum = fibonacci_sum_naive(to)
    from_sum = fibonacci_sum_naive(from_ - 1)

    return (to_sum - from_sum) % 10


if __name__ == '__main__':
    # input = sys.stdin.read();
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))
