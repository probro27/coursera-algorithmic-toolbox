# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    if len(weights) == 0 or capacity == 0:
        return 0
    
    costs = [(x,y) for x, y in zip(values, weights)]
    costs.sort(key=lambda x: x[0]/x[1], reverse=True)

    # print(costs)
    value = 0
    while capacity > 0 and len(costs) > 0:
        tupple = costs[0]
        if tupple[1] > capacity:
            value += capacity * tupple[0] / tupple[1]
            capacity = 0
        else:
            value += tupple[0]
            capacity -= tupple[1]
        costs.pop(0)
    
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    # print(opt_value)
    print("{:.10f}".format(opt_value))
