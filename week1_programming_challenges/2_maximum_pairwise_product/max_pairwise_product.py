def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    first_max = 0
    second_max = 0
    first_max_index = 0
    for i in range(n):
        if numbers[i] > first_max:
            first_max = numbers[i]
            first_max_index = i
    
    for i in range(n):
        if i != first_max_index and numbers[i] > second_max:
            second_max = numbers[i]
    
    max_product = first_max * second_max
    return max_product

def main():
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

if __name__ == '__main__':
    main()
