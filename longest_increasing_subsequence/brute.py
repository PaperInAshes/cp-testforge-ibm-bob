"""
brute.py — O(N^2) DP solution for LIS (correct for small N).
Reads from stdin.
"""
import sys


def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    A = [int(input_data[idx + i]) for i in range(N)]; idx += N

    if N == 0:
        print(0)
        return

    # dp[i] = length of LIS ending at index i
    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

    print(max(dp))


if __name__ == "__main__":
    solve()
