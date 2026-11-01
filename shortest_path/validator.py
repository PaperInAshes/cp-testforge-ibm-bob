#!/usr/bin/env python3
"""
validator.py - Memeriksa format dan constraints file input Shortest Path.
Usage: python3 validator.py < input.in
       python3 validator.py input.in
"""
import sys

def error(msg):
    print(f"INVALID: {msg}", file=sys.stderr)
    sys.exit(1)

def validate(lines):
    # Hilangkan trailing whitespace dan baris kosong di akhir
    while lines and lines[-1].strip() == '':
        lines.pop()

    if len(lines) == 0:
        error("File kosong")

    # Baris pertama: N M
    parts = lines[0].split()
    if len(parts) != 2:
        error(f"Baris 1 harus berisi tepat 2 bilangan, ditemukan: {len(parts)}")
    try:
        N, M = int(parts[0]), int(parts[1])
    except ValueError:
        error(f"N dan M harus bilangan bulat, ditemukan: '{lines[0].strip()}'")

    if not (2 <= N <= 100000):
        error(f"N={N} di luar range [2, 100000]")
    if not (1 <= M <= 200000):
        error(f"M={M} di luar range [1, 200000]")

    # Jumlah baris
    expected_lines = 1 + M
    if len(lines) != expected_lines:
        error(f"Diharapkan {expected_lines} baris (1 header + {M} sisi), ditemukan {len(lines)}")

    # Setiap sisi
    for i in range(1, M + 1):
        edge_parts = lines[i].split()
        if len(edge_parts) != 3:
            error(f"Baris {i+1} harus berisi tepat 3 bilangan (u v w), ditemukan: {len(edge_parts)}")
        try:
            u, v, w = int(edge_parts[0]), int(edge_parts[1]), int(edge_parts[2])
        except ValueError:
            error(f"Baris {i+1}: u, v, w harus bilangan bulat")

        if not (1 <= u <= N):
            error(f"Baris {i+1}: u={u} di luar range [1, {N}]")
        if not (1 <= v <= N):
            error(f"Baris {i+1}: v={v} di luar range [1, {N}]")
        if not (1 <= w <= 1000000000):
            error(f"Baris {i+1}: w={w} di luar range [1, 1000000000]")

    print("OK")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            data = f.readlines()
    else:
        data = sys.stdin.readlines()
    lines = [line.rstrip('\n') for line in data]
    validate(lines)
