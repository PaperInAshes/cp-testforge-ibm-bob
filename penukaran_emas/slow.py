#!/usr/bin/env python3
"""
slow.py — Solusi BENAR tetapi lambat (rekursi murni tanpa memoization,
dengan penambahan busy-wait untuk memastikan TLE pada input besar).

Untuk soal ini N ≤ 1000 dan rekursi murni masih cepat secara asimtotik
(depth log N, branching factor 3), sehingga rekursi murni saja mungkin
tidak TLE pada N=1000. Oleh karena itu slow.py menambahkan loop iterasi
dummy besar pada setiap call rekursi untuk mensimulasikan TLE.

CATATAN: Ini adalah simulasi artificially slow. Dalam konteks soal nyata,
"slow" biasanya dari kompleksitas algoritmik yang salah (misal: iterasi semua
nilai 0..N tanpa DP proper, atau rekursi ulang tanpa memoization pada subproblem
yang tumpang tindih banyak). Karena N ≤ 1000 membuat rekursi murni masih O(N log N)
kurang lebih, slow.py memakai heavy per-call work.
"""
import sys

def f_slow(n):
    """Rekursi murni + pekerjaan dummy untuk mensimulasikan lambatnya."""
    if n <= 0:
        return 0
    # Pekerjaan dummy: kalkulasi tidak berguna untuk memperlambat
    dummy = sum(range(50000))  # ~50k operasi per call rekursi
    _ = dummy  # suppress unused warning
    
    keep = n
    exchange = f_slow(n // 2) + f_slow(n // 3) + f_slow(n // 4)
    return max(keep, exchange)

def main():
    N = int(sys.stdin.read().strip())
    print(f_slow(N))

if __name__ == "__main__":
    main()
