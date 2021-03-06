# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments.sort(key = lambda x: x[1])
    n = len(segments)
    i = 0
    while i < n:
        curr = segments[i]
        while i < n - 1 and segments[i + 1].start <= curr.end:
            i += 1
        points.append(curr.end)
        i += 1
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
