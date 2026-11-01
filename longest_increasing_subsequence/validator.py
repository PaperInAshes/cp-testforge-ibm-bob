"""
validator.py — Validates a single input file for the LIS problem.
Usage: python3 validator.py <input_file>
Exit 0 = valid, Exit 1 = invalid (prints reason).
"""
import sys


def validate(filepath):
    with open(filepath, "r") as f:
        lines = f.read().splitlines()

    # Strip trailing blank lines
    while lines and lines[-1].strip() == "":
        lines.pop()

    if len(lines) < 1:
        print(f"INVALID: file is empty")
        return False

    # --- Line 1: N ---
    parts0 = lines[0].split()
    if len(parts0) != 1:
        print(f"INVALID: line 1 must contain exactly one integer N, got: {lines[0]!r}")
        return False
    try:
        N = int(parts0[0])
    except ValueError:
        print(f"INVALID: N is not an integer: {parts0[0]!r}")
        return False

    if not (1 <= N <= 100_000):
        print(f"INVALID: N={N} out of range [1, 100000]")
        return False

    # --- Line 2: A[0..N-1] ---
    if N == 0:
        # N=0 not allowed by constraints (N>=1), guard only
        print("INVALID: N must be >= 1")
        return False

    if len(lines) < 2:
        print("INVALID: missing line 2 (array of N integers)")
        return False

    parts1 = lines[1].split()
    if len(parts1) != N:
        print(f"INVALID: line 2 has {len(parts1)} numbers, expected {N}")
        return False

    for i, tok in enumerate(parts1):
        try:
            v = int(tok)
        except ValueError:
            print(f"INVALID: A[{i}]={tok!r} is not an integer")
            return False
        if not (-1_000_000_000 <= v <= 1_000_000_000):
            print(f"INVALID: A[{i}]={v} out of range [-1e9, 1e9]")
            return False

    if len(lines) > 2:
        # Allow extra blank lines but not extra content
        extra = [l for l in lines[2:] if l.strip() != ""]
        if extra:
            print(f"INVALID: unexpected extra lines after line 2: {extra[:3]}")
            return False

    print(f"OK: N={N}, {len(parts1)} values")
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 validator.py <input_file>")
        sys.exit(1)
    ok = validate(sys.argv[1])
    sys.exit(0 if ok else 1)
