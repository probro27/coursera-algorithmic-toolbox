# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    if n == 1:
        return [1]
    if n == 2:
        return [2]
    num = n
    index = 1
    while num > 0:
        if num > 2 * index:
            summands.append(index)
            num -= index
        else:
            summands.append(num)
            num = 0
        index += 1
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
