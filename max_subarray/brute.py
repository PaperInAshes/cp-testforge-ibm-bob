"""
brute.py  –  O(N^2) brute-force solution (guaranteed correct)
Usage: python brute.py < input_file
"""
import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    A = [int(input_data[idx + i]) for i in range(N)]; idx += N

    best = A[0]
    for i in range(N):
        s = 0
        for j in range(i, N):
            s += A[j]
            if s > best:
                best = s
    print(best)

if __name__ == '__main__':
    solve()
