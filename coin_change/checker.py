"""
checker.py — Output checker for Coin Change.

Note: Coin Change has a UNIQUE answer (minimum coin count is unique),
so simple text comparison suffices. This checker is provided as a
convenience and for future extensibility.

Usage: python3 checker.py <input.in> <expected.out> <actual.out>
Exit 0 = correct, Exit 1 = wrong.
"""
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: checker.py <input.in> <expected.out> <actual.out>", file=sys.stderr)
        sys.exit(2)

    _, input_file, expected_file, actual_file = sys.argv

    try:
        expected = open(expected_file).read().strip()
        actual = open(actual_file).read().strip()
    except FileNotFoundError as e:
        print(f"File not found: {e}", file=sys.stderr)
        sys.exit(2)

    # Both must be a single integer
    try:
        exp_val = int(expected)
        act_val = int(actual)
    except ValueError:
        print(f"WRONG: non-integer output (expected={expected!r}, actual={actual!r})")
        sys.exit(1)

    if exp_val == act_val:
        print(f"OK (answer={exp_val})")
        sys.exit(0)
    else:
        print(f"WRONG: expected={exp_val}, got={act_val}")
        sys.exit(1)

if __name__ == '__main__':
    main()
