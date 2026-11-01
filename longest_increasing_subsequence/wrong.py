"""
wrong.py — INTENTIONALLY BUGGY solution.
Bug: uses bisect_right instead of bisect_left, which allows equal elements
     into the tails array (effectively computing non-strictly increasing LIS).
This gives WRONG answers when the array contains duplicate elements.
"""
import sys
from bisect import bisect_right  # BUG: should be bisect_left for STRICT increasing


def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    A = [int(input_data[idx + i]) for i in range(N)]

    tails = []
    for x in A:
        # BUG: bisect_right allows equal element to extend the subsequence,
        # so [1,1,1] would give length 3 instead of correct answer 1.
        pos = bisect_right(tails, x)
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x

    print(len(tails))


if __name__ == "__main__":
    solve()
