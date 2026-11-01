"""
sol.py  –  O(N) Kadane's algorithm solution
Usage: python sol.py < input_file
"""
import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    A = [int(input_data[idx + i]) for i in range(N)]; idx += N

    best = A[0]
    cur  = A[0]
    for i in range(1, N):
        if cur < 0:
            cur = A[i]
        else:
            cur += A[i]
        if cur > best:
            best = cur
    print(best)

if __name__ == '__main__':
    solve()
