#!/usr/bin/env python3
"""
wrong.py - Solusi SALAH dengan bug umum:
Bug 1: Menggunakan BFS biasa (tanpa mempertimbangkan bobot sisi),
       sehingga mengasumsikan semua bobot sama.
       Akan memberi jawaban salah ketika bobot berbeda-beda.
Bug 2: Tidak menangani graf tak terhubung (akan crash atau output salah).
"""
import sys
from collections import deque
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    # BFS biasa - SALAH karena tidak mempertimbangkan bobot
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0
    queue = deque([1])

    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if dist[v] == INF:
                dist[v] = dist[u] + w  # Bug: ini bukan shortest path berbobot!
                queue.append(v)

    # Bug: tidak menangani -1 untuk tak terhubung dengan benar
    # (sebenarnya secara kebetulan benar untuk kasus ini, tapi logika BFS salah)
    ans = dist[N]
    print(-1 if ans == INF else ans)

if __name__ == "__main__":
    main()
