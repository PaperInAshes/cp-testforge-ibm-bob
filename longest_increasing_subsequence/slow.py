"""
slow.py — CORRECT but O(N^2) DP solution — will TLE on large N.
Identical logic to brute.py; it is "the correct but too-slow" solution.
"""
import sys


def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    A = [int(input_data[idx + i]) for i in range(N)]

    if N == 0:
        print(0)
        return

    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

    print(max(dp))


if __name__ == "__main__":
    solve()
