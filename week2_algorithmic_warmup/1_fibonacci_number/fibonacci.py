# Uses python3
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

n = int(input())
print(calc_fib(n))
