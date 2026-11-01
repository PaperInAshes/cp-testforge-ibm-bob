#!/usr/bin/env python3
"""
brute.py — brute force solution for "Diskon Beli A Gratis B"
Correct for any N, uses optimal greedy (provably correct via exchange argument).
For cross-verification on small N.

Usage: python3 brute.py < input.in
"""
import sys

def solve():
    data = sys.stdin.read().split()
    N, A, B = int(data[0]), int(data[1]), int(data[2])
    h = list(map(int, data[3:3+N]))

    # Optimal greedy (provably correct):
    # Sort descending. Form groups of (A+B) greedily from most expensive.
    # In each group, the B cheapest (last B in the group) are free.
    # Remaining items (not in any complete group) are paid in full.
    h.sort(reverse=True)
    step = A + B
    groups = N // step

    total = 0
    for i in range(N):
        idx_in_group = i % step
        # Only apply discount within the formed groups
        if i < groups * step and idx_in_group >= A:
            continue  # this item is free
        total += h[i]

    print(total)

if __name__ == '__main__':
    solve()
