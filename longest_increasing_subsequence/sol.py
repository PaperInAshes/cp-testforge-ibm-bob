"""
sol.py — O(N log N) efficient solution for LIS using patience sorting.
Reads from stdin.
"""
import sys
from bisect import bisect_left


def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    A = [int(input_data[idx + i]) for i in range(N)]

    # tails[i] = smallest tail element of all increasing subsequences of length i+1
    tails = []
    for x in A:
        pos = bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x

    print(len(tails))


if __name__ == "__main__":
    solve()
