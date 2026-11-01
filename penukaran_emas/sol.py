#!/usr/bin/env python3
"""
sol.py — Solusi efisien dengan memoization (top-down DP).
f(n) = max(n, f(n//2) + f(n//3) + f(n//4))
Kompleksitas: O(N) state, O(1) per state → O(N) total.
"""
import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def f(n):
    if n <= 0:
        return 0
    keep = n
    exchange = f(n // 2) + f(n // 3) + f(n // 4)
    return max(keep, exchange)

def main():
    N = int(sys.stdin.read().strip())
    print(f(N))

if __name__ == "__main__":
    main()
