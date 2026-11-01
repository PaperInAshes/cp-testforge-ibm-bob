"""
wrong.py  –  INTENTIONALLY INCORRECT solution.
Bug: initializes best = 0 instead of A[0].
This causes it to return 0 for all-negative arrays,
which is wrong (correct answer should be the largest negative element).
"""
import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    A = [int(input_data[idx + i]) for i in range(N)]; idx += N

    best = 0   # BUG: should be A[0]
    cur  = 0   # BUG: should be A[0]
    for i in range(N):
        cur += A[i]
        if cur > best:
            best = cur
        if cur < 0:
            cur = 0
    print(best)

if __name__ == '__main__':
    solve()
