#!/usr/bin/env python3
"""
brute.py — Solusi brute force rekursi murni (tanpa memoization).
Pasti benar untuk input kecil. Kecepatan tidak diprioritaskan.
"""
import sys

def f(n):
    """Rekursi murni tanpa cache — benar tapi lambat."""
    if n <= 0:
        return 0
    # Pilihan 1: tidak tukar
    keep = n
    # Pilihan 2: tukar jadi tiga keping
    exchange = f(n // 2) + f(n // 3) + f(n // 4)
    return max(keep, exchange)

def main():
    N = int(sys.stdin.read().strip())
    print(f(N))

if __name__ == "__main__":
    main()
