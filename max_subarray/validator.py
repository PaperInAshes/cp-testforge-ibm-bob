"""
validator.py
Checks that an input file satisfies the problem constraints:
  - Line 1: integer N with 1 <= N <= 100000
  - Line 2: exactly N integers, each in [-1e9, 1e9]
Usage: python validator.py <input_file>
Exit code 0 = valid, 1 = invalid.
"""
import sys

def validate(path):
    try:
        with open(path) as f:
            content = f.read()
    except FileNotFoundError:
        print(f"ERROR: file not found: {path}")
        return False

    lines = content.split('\n')
    # Strip trailing empty lines
    while lines and lines[-1].strip() == '':
        lines.pop()

    if len(lines) != 2:
        print(f"ERROR [{path}]: expected exactly 2 non-empty lines, got {len(lines)}")
        return False

    # --- Line 1: N ---
    try:
        N = int(lines[0].strip())
    except ValueError:
        print(f"ERROR [{path}]: line 1 is not an integer: {lines[0]!r}")
        return False

    if not (1 <= N <= 100_000):
        print(f"ERROR [{path}]: N={N} out of range [1, 100000]")
        return False

    # --- Line 2: N integers ---
    tokens = lines[1].split()
    if len(tokens) != N:
        print(f"ERROR [{path}]: expected {N} integers on line 2, got {len(tokens)}")
        return False

    for i, tok in enumerate(tokens):
        try:
            v = int(tok)
        except ValueError:
            print(f"ERROR [{path}]: token {i+1} is not an integer: {tok!r}")
            return False
        if not (-1_000_000_000 <= v <= 1_000_000_000):
            print(f"ERROR [{path}]: A[{i+1}]={v} out of range [-1e9, 1e9]")
            return False

    print(f"OK [{path}]: N={N}")
    return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python validator.py <input_file> [<input_file2> ...]")
        sys.exit(1)

    all_ok = True
    for path in sys.argv[1:]:
        if not validate(path):
            all_ok = False

    sys.exit(0 if all_ok else 1)
