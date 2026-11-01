#!/usr/bin/env python3
"""
sol.py - Solusi efisien menggunakan Dijkstra dengan priority queue.
Kompleksitas: O((N + M) log N)
"""
import sys
import heapq
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        adj[u].append((w, v))
        adj[v].append((w, u))  # tak berarah

    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0

    # Min-heap: (jarak, simpul)
    heap = [(0, 1)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue  # sudah ada jalur lebih pendek
        if u == N:
            break
        for w, v in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    ans = dist[N]
    print(-1 if ans == INF else ans)

if __name__ == "__main__":
    main()
