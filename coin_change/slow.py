"""
slow.py — CORRECT but SLOW solution (will TLE on large inputs).
Uses top-down recursion WITHOUT memoization.
Complexity: exponential O(N^X) in worst case.
Will TLE on X=10000 with small coins.
"""
import sys
sys.setrecursionlimit(1000000)

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    X = int(input_data[idx]); idx += 1
    coins = [int(input_data[idx + i]) for i in range(N)]

    def rec(remaining):
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')
        best = float('inf')
        for c in coins:
            if c <= remaining:
                res = rec(remaining - c)
                if res != float('inf'):
                    best = min(best, res + 1)
        return best

    result = rec(X)
    print(-1 if result == float('inf') else result)

if __name__ == '__main__':
    solve()
