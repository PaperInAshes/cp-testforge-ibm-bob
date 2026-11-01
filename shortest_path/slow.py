#!/usr/bin/env python3
"""
slow.py - Solusi BENAR tapi LAMBAT.
Implementasi Dijkstra tanpa priority queue (naive O(N^2 + M)),
ditambah re-scanning semua simpul setiap iterasi.
Pada N=100000, M=200000 ini akan TLE.
"""
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0
    visited = [False] * (N + 1)

    # Dijkstra tanpa heap - O(N^2): setiap iterasi cari minimum secara linear
    for _ in range(N):
        # Cari simpul belum dikunjungi dengan dist terkecil - O(N)
        u = -1
        for i in range(1, N + 1):
            if not visited[i] and dist[i] != INF:
                if u == -1 or dist[i] < dist[u]:
                    u = i

        if u == -1:
            break

        visited[u] = True

        # Update tetangga
        for v, w in adj[u]:
            if not visited[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    ans = dist[N]
    print(-1 if ans == INF else ans)

if __name__ == "__main__":
    main()
