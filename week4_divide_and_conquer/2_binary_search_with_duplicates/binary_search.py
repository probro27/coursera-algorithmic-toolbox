def binary_search(keys, query):
    # write your code here
    low = 0
    high = len(keys)
    flag = 0
    while low != high:
        mid = (low + high) // 2
        if keys[mid] < query:
            low = mid + 1
        else:
            if keys[mid] == query:
                flag = 1
            high = mid
    
    if flag == 1:
        return low
    else:
        return -1
    


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
