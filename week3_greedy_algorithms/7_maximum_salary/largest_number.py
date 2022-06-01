#Uses python3

from cmath import inf
import sys

def isGreaterOrEqual(digit, maxDigit):
    digitStr = str(digit)
    maxDigitStr = str(maxDigit)
    if len(digitStr) < len(maxDigitStr):
        if digitStr[0] > maxDigitStr[0]:
            return True
        elif digitStr[0] < maxDigitStr[0]:
            return False
        else:
            i = 1
            for i in range(1, len(digitStr)):
                if digitStr[i] < maxDigitStr[i]:
                    return False
                elif digitStr[i] > maxDigitStr[i]:
                    return True
            if maxDigitStr[i] < maxDigitStr[i - 1]:
                return True
            else:
                return False
    elif len(digitStr) > len(maxDigitStr):
        if digitStr[0] > maxDigitStr[0]:
            return True
        elif digitStr[0] < maxDigitStr[0]:
            return False
        else:
            i = 1
            for i in range(1, len(maxDigitStr)):
                if digitStr[i] < maxDigitStr[i]:
                    return False
                elif digitStr[i] > maxDigitStr[i]:
                    return True
            if digitStr[i] < digitStr[i - 1]:
                return False
            else:
                return True
    else:
        return digitStr >= maxDigitStr

def largest_number(a):
    #write your code here
    res = ""
    while len(a) != 0:
        maxDigit = 0 
        for i in range(len(a)):
            if isGreaterOrEqual(int(a[i]), maxDigit):
                maxDigit = a[i]
        res = res + maxDigit
        # print(maxDigit)
        a.remove(maxDigit)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    # print(isGreaterOrEqual(2, 21))
    
