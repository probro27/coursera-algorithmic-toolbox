# Uses python3
import sys

def countFrequency(a, element, left, right):
    count = 0
    for i in range(left, right + 1):
        if a[i] == element:
            count += 1
    return count

def get_majority_element(a, left, right):
    if left > right:
        return -1
    if left == right:
        return a[left]
    #write your code here
    mid = (left + right) // 2
    left_majority = get_majority_element(a, left, mid)
    right_majority = get_majority_element(a, mid + 1, right)
    left_count = countFrequency(a, left_majority, left, right)
    right_count = countFrequency(a, right_majority, left, right)
    if left_majority == right_majority:
        return left_majority
    if left_count > (right - left + 1) // 2:
        return left_majority
    if right_count > (right - left + 1) // 2:
        return right_majority
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n - 1) != -1:
        print(1)
    else:
        print(0)
