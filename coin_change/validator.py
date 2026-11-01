"""
validator.py — Validates a Coin Change input file.
Usage: python3 validator.py < input.in
       python3 validator.py input.in
Exit 0 = valid, Exit 1 = invalid (error message printed to stderr).
"""
import sys

def error(msg):
    print(f"INVALID: {msg}", file=sys.stderr)
    sys.exit(1)

def main():
    if len(sys.argv) == 2:
        try:
            data = open(sys.argv[1]).read()
        except FileNotFoundError:
            error(f"File not found: {sys.argv[1]}")
    else:
        data = sys.stdin.read()

    lines = data.strip().split('\n')

    # Must have exactly 2 lines
    if len(lines) != 2:
        error(f"Expected 2 lines, got {len(lines)}")

    # Line 1: N and X
    parts1 = lines[0].split()
    if len(parts1) != 2:
        error(f"Line 1 must have exactly 2 integers, got {len(parts1)}")

    try:
        N = int(parts1[0])
        X = int(parts1[1])
    except ValueError:
        error("Line 1 must contain integers only")

    if not (1 <= N <= 100):
        error(f"N={N} out of range [1, 100]")
    if not (1 <= X <= 10000):
        error(f"X={X} out of range [1, 10000]")

    # Line 2: N coin values
    parts2 = lines[1].split()
    if len(parts2) != N:
        error(f"Line 2 must have exactly N={N} integers, got {len(parts2)}")

    coins = []
    for token in parts2:
        try:
            c = int(token)
        except ValueError:
            error(f"Coin value '{token}' is not an integer")
        if not (1 <= c <= 10000):
            error(f"Coin value {c} out of range [1, 10000]")
        coins.append(c)

    # All coin values must be distinct
    if len(coins) != len(set(coins)):
        error(f"Coin values must all be distinct, got duplicates: {coins}")

    print("OK")
    sys.exit(0)

if __name__ == '__main__':
    main()
