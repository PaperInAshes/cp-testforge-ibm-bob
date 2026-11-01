"""
wrong.py — INTENTIONALLY WRONG solution.
Bug: Uses greedy (always pick largest coin <= remaining).
This fails on non-canonical coin systems (e.g. {1,3,4}, X=6 → greedy=3, optimal=2).
Also may fail to detect impossibility correctly.
"""
import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    X = int(input_data[idx]); idx += 1
    coins = sorted([int(input_data[idx + i]) for i in range(N)], reverse=True)

    remaining = X
    count = 0
    for c in coins:
        while remaining >= c:
            remaining -= c
            count += 1

    if remaining == 0:
        print(count)
    else:
        # BUG: prints 0 instead of -1 when greedy fails to reach exact X
        # (greedy might overshoot or get stuck — here it just outputs wrong count)
        print(0)

if __name__ == '__main__':
    solve()
