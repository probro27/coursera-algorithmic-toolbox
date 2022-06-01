# python3
import sys


def compute_min_refills(location, distance, tank, stops):
    # write your code here
    if location + tank >= distance:
        return 0
    if len(stops) == 0 or (stops[0] - location > tank):
        print(-1)
        quit()
    lastStop = location
    while len(stops) != 0 and (stops[0] - location) <= tank:
        lastStop = stops[0]
        stops.pop(0)
    return 1 + compute_min_refills(lastStop, distance, tank, stops)

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(0, d, m, stops))
