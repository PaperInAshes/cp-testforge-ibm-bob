"""
brute.py — Correct but slow brute-force solution for Coin Change.
Uses BFS (exact minimum coins) — guaranteed correct for small inputs.
Complexity: O(X * N) in BFS levels, but uses explicit BFS queue.
"""
import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    X = int(input_data[idx]); idx += 1
    coins = [int(input_data[idx + i]) for i in range(N)]
    idx += N

    # BFS: each level = number of coins used
    visited = [False] * (X + 1)
    queue = deque()
    queue.append((0, 0))  # (current_sum, num_coins)
    visited[0] = True

    while queue:
        total, count = queue.popleft()
        if total == X:
            print(count)
            return
        for c in coins:
            nxt = total + c
            if nxt <= X and not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, count + 1))

    print(-1)

if __name__ == '__main__':
    solve()
