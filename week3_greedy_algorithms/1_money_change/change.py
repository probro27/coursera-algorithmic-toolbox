# Uses python3
import sys

def get_change(m):
    #write your code here
    
    numCoins = m // 10 + (m % 10) // 5 + (m % 5) // 1

    return numCoins

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
