#!/usr/bin/env python3
"""
validator.py — validates input files for "Diskon Beli A Gratis B"
Usage: python3 validator.py < file.in
       python3 validator.py file.in   (reads from file argument)
Exits 0 if valid, 1 if invalid (with error message to stderr).
"""
import sys

def validate(data: str, filename: str = "<stdin>"):
    lines = data.strip().split('\n')
    assert len(lines) >= 2, "Expected at least 2 lines"

    # Line 1: N A B
    parts1 = lines[0].split()
    assert len(parts1) == 3, f"Line 1 must have exactly 3 integers, got {len(parts1)}"
    N, A, B = int(parts1[0]), int(parts1[1]), int(parts1[2])

    assert 1 <= N <= 100000, f"N={N} out of range [1, 100000]"
    assert 1 <= A <= 100000, f"A={A} out of range [1, 100000]"
    assert 1 <= B <= 100000, f"B={B} out of range [1, 100000]"

    # Line 2: N integers h_i
    parts2 = lines[1].split()
    assert len(parts2) == N, f"Line 2 must have exactly N={N} integers, got {len(parts2)}"

    for i, s in enumerate(parts2):
        hi = int(s)
        assert 1 <= hi <= 1_000_000_000, f"h[{i+1}]={hi} out of range [1, 1000000000]"

    # No extra lines (beyond trailing whitespace)
    extra = '\n'.join(lines[2:]).strip()
    assert extra == '', f"Extra content after line 2: {repr(extra[:50])}"

    print(f"[OK] {filename}: N={N} A={A} B={B}")
    return True


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            data = f.read()
        fname = sys.argv[1]
    else:
        data = sys.stdin.read()
        fname = "<stdin>"

    try:
        validate(data, fname)
        sys.exit(0)
    except AssertionError as e:
        print(f"[INVALID] {fname}: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] {fname}: {e}", file=sys.stderr)
        sys.exit(1)
