"""
run_tests.py — Test runner for Coin Change solutions.
Supports .py (Python 3) and .cpp (compiled with g++).

Usage:
    python3 run_tests.py <solution_file>
    python3 run_tests.py sol.py
    python3 run_tests.py my_solution.cpp

Reports PASS / WA / TLE / RE per test.
Time limit: 1 second (as per problem statement).
"""
import sys
import os
import subprocess
import glob
import time
import shutil
import tempfile

TIME_LIMIT = 1.0  # seconds
TESTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests")

def compile_cpp(source_file):
    """Compile a C++ file. Returns path to binary or None on failure."""
    if not shutil.which("g++"):
        print("ERROR: g++ not found. Cannot compile C++ solution.", file=sys.stderr)
        return None
    binary = tempfile.mktemp(suffix=".out", dir=TESTS_DIR)
    result = subprocess.run(
        ["g++", "-O2", "-o", binary, source_file],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Compilation FAILED:\n{result.stderr}", file=sys.stderr)
        return None
    print(f"  Compiled: {source_file} → {binary}")
    return binary

def run_solution(cmd, input_data, tl):
    """Run solution command with input, return (stdout, stderr, elapsed, verdict)."""
    start = time.perf_counter()
    try:
        proc = subprocess.run(
            cmd,
            input=input_data,
            capture_output=True,
            text=True,
            timeout=tl * 3  # give 3x TL before hard kill for TLE detection
        )
        elapsed = time.perf_counter() - start
        if proc.returncode != 0:
            return proc.stdout.strip(), proc.stderr.strip(), elapsed, "RE"
        return proc.stdout.strip(), proc.stderr.strip(), elapsed, "OK"
    except subprocess.TimeoutExpired:
        elapsed = time.perf_counter() - start
        return "", "Timeout (hard kill)", elapsed, "TLE"

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 run_tests.py <solution_file>")
        sys.exit(1)

    solution = sys.argv[1]
    if not os.path.isfile(solution):
        print(f"ERROR: Solution file not found: {solution}")
        sys.exit(1)

    ext = os.path.splitext(solution)[1].lower()

    if ext == ".py":
        cmd = [sys.executable, solution]
        binary = None
    elif ext == ".cpp":
        binary = compile_cpp(solution)
        if binary is None:
            sys.exit(1)
        cmd = [binary]
    else:
        print(f"ERROR: Unsupported file extension: {ext} (use .py or .cpp)")
        sys.exit(1)

    # Find all test inputs, sorted
    test_inputs = sorted(glob.glob(os.path.join(TESTS_DIR, "*.in")))
    if not test_inputs:
        print("No test inputs found in tests/")
        sys.exit(1)

    print(f"\n{'='*65}")
    print(f"  Running: {solution}")
    print(f"  Time limit: {TIME_LIMIT}s")
    print(f"  Tests: {len(test_inputs)}")
    print(f"{'='*65}")
    print(f"  {'#':<3}  {'Test':<40}  {'Result':<6}  {'Time':>7}  {'Note'}")
    print(f"  {'-'*3}  {'-'*40}  {'-'*6}  {'-'*7}  {'-'*20}")

    results = {"PASS": 0, "WA": 0, "TLE": 0, "RE": 0}

    for i, inp_path in enumerate(test_inputs, 1):
        name = os.path.basename(inp_path).replace(".in", "")
        out_path = inp_path.replace(".in", ".out")

        input_data = open(inp_path).read()
        expected = open(out_path).read().strip() if os.path.isfile(out_path) else None

        actual, stderr, elapsed, verdict = run_solution(cmd, input_data, TIME_LIMIT)

        if verdict == "RE":
            status = "RE"
            note = f"stderr: {stderr[:40]}" if stderr else "non-zero exit"
        elif verdict == "TLE" or elapsed > TIME_LIMIT:
            status = "TLE"
            note = f">{TIME_LIMIT}s"
        elif expected is None:
            status = "PASS"  # No expected output yet
            note = "no .out"
        elif actual == expected:
            status = "PASS"
            note = ""
        else:
            status = "WA"
            note = f"expected={expected!r} got={actual!r}"[:50]

        results[status] = results.get(status, 0) + 1
        time_str = f"{elapsed*1000:.1f}ms"
        print(f"  {i:<3}  {name:<40}  {status:<6}  {time_str:>7}  {note}")

    print(f"{'='*65}")
    print(f"  SUMMARY: PASS={results.get('PASS',0)}  WA={results.get('WA',0)}  "
          f"TLE={results.get('TLE',0)}  RE={results.get('RE',0)}")
    print(f"{'='*65}\n")

    # Cleanup compiled binary
    if binary and os.path.isfile(binary):
        os.remove(binary)

    # Exit code: 0 if all passed, 1 otherwise
    total = len(test_inputs)
    passed = results.get("PASS", 0)
    sys.exit(0 if passed == total else 1)

if __name__ == '__main__':
    main()
