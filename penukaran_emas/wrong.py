#!/usr/bin/env python3
"""
wrong.py — Solusi SALAH dengan bug paling umum:
BUG: Hanya memeriksa satu level penukaran, tidak merekursi lebih dalam.
Artinya f(n) = max(n, n//2 + n//3 + n//4) — tanpa rekursi pada pecahan.
Ini salah karena pecahan yang dihasilkan mungkin juga menguntungkan untuk ditukar lagi.

Contoh kegagalan: N=24
- wrong.py: max(24, 12+8+6) = max(24, 26) = 26
- sol.py:   f(12)=13, f(8)=8, f(6)=6 → 13+8+6 = 27
Jadi wrong.py akan output 26, sol.py output 27.
"""
import sys

def f_wrong(n):
    """Satu level saja, tidak rekursif pada pecahan."""
    if n <= 0:
        return 0
    keep = n
    # BUG: langsung jumlahkan n//2 + n//3 + n//4, bukan f(n//2)+f(n//3)+f(n//4)
    exchange = (n // 2) + (n // 3) + (n // 4)
    return max(keep, exchange)

def main():
    N = int(sys.stdin.read().strip())
    print(f_wrong(N))

if __name__ == "__main__":
    main()
