#!/usr/bin/env python3
"""
validator.py — Memvalidasi format dan constraints file input soal Penukaran Emas.
Usage: python3 validator.py < input.in
Exit 0 jika valid, exit 1 jika tidak valid.
"""
import sys

def main():
    data = sys.stdin.read().split()
    
    # Harus tepat 1 token
    if len(data) != 1:
        print(f"ERROR: Expected exactly 1 token, got {len(data)}", file=sys.stderr)
        sys.exit(1)
    
    # Harus integer
    try:
        N = int(data[0])
    except ValueError:
        print(f"ERROR: Token is not an integer: '{data[0]}'", file=sys.stderr)
        sys.exit(1)
    
    # Harus 10 <= N <= 1000
    if N < 10 or N > 1000:
        print(f"ERROR: N={N} out of range [10, 1000]", file=sys.stderr)
        sys.exit(1)
    
    print("OK")
    sys.exit(0)

if __name__ == "__main__":
    main()
