"""
sol.py — Efficient correct solution for Coin Change.
Uses bottom-up DP (Unbounded Knapsack style).
Complexity: O(N * X) — fast enough for N=100, X=10000.
"""
import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    X = int(input_data[idx]); idx += 1
    coins = [int(input_data[idx + i]) for i in range(N)]

    INF = float('inf')
    dp = [INF] * (X + 1)
    dp[0] = 0  # base case: 0 coins needed to make sum 0

    for j in range(1, X + 1):
        for c in coins:
            if c <= j and dp[j - c] != INF:
                dp[j] = min(dp[j], dp[j - c] + 1)

    print(-1 if dp[X] == INF else dp[X])

if __name__ == '__main__':
    solve()
