#!/usr/bin/env python3
"""
brute.py - Solusi pasti benar untuk input kecil.
Menggunakan Bellman-Ford O(N*M), lambat tapi benar.
"""
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
        edges.append((v, u, w))  # tak berarah

    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0

    # Bellman-Ford: relaksasi N-1 kali
    for _ in range(N - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    ans = dist[N]
    print(-1 if ans == INF else ans)

if __name__ == "__main__":
    main()
