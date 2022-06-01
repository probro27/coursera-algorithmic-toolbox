# Uses python3


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    fibn = 0
    fibn_1 = 1
    fibn_2 = 1

    for i in range(2, n + 1):
        fibn_2 = (fibn_1 + fibn) % 10
        fibn = fibn_1
        fibn_1 = fibn_2

    return fibn_2
    

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
