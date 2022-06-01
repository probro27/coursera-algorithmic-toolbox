# Uses python3
import sys

def gcd_iterative(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a

def lcm_naive(a, b):
    return a * b // gcd_iterative(a, b)

if __name__ == '__main__':
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    print(lcm_naive(a, b))

