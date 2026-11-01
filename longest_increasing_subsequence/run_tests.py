"""
run_tests.py — Run all tests in tests/ against a solution file.
Supports .py (Python 3) and .cpp (compiled with g++).
Reports PASS / WA / TLE / RE per test.

Usage:
  python3 run_tests.py <solution_file>

Examples:
  python3 run_tests.py sol.py
  python3 run_tests.py my_solution.cpp
"""
import os
import sys
import subprocess
import glob
import shutil
import time
import tempfile

TIME_LIMIT = 1.0          # seconds (matches problem TLE)
TLE_MARGIN = 1.5          # allow 1.5× for interpreter/OS overhead on Python
TESTS_DIR  = os.path.join(os.path.dirname(__file__), "tests")


def compile_cpp(src):
    """Compile a C++ file; return (exe_path, error_msg)."""
    exe = src.replace(".cpp", "") + "_bin"
    result = subprocess.run(
        ["g++", "-O2", "-o", exe, src],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return None, result.stderr
    return exe, None


def run_one(cmd, input_path, time_limit):
    """
    Run command with stdin from input_path.
    Returns (stdout, status) where status in {PASS-pending, TLE, RE}.
    """
    try:
        with open(input_path, "r") as fin:
            start = time.perf_counter()
            proc = subprocess.run(
                cmd,
                stdin=fin,
                capture_output=True,
                text=True,
                timeout=time_limit
            )
            elapsed = time.perf_counter() - start
    except subprocess.TimeoutExpired:
        return None, "TLE", time_limit
    except Exception as e:
        return None, f"RE({e})", 0.0

    if proc.returncode != 0:
        return None, f"RE(exit {proc.returncode})", elapsed

    return proc.stdout.strip(), "OK", elapsed


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 run_tests.py <solution_file>")
        sys.exit(1)

    sol_file = sys.argv[1]
    if not os.path.isfile(sol_file):
        print(f"Error: file not found: {sol_file}")
        sys.exit(1)

    ext = os.path.splitext(sol_file)[1].lower()
    exe_cleanup = None

    if ext == ".py":
        cmd = [sys.executable, sol_file]
        effective_limit = TIME_LIMIT * TLE_MARGIN  # generous for Python interpreter
    elif ext == ".cpp":
        if not shutil.which("g++"):
            print("Error: g++ not found. Cannot compile C++ solution.")
            sys.exit(1)
        exe, err = compile_cpp(sol_file)
        if err:
            print(f"Compilation error:\n{err}")
            sys.exit(1)
        cmd = [exe]
        exe_cleanup = exe
        effective_limit = TIME_LIMIT
    else:
        print(f"Unsupported file extension: {ext}  (use .py or .cpp)")
        sys.exit(1)

    test_files = sorted(glob.glob(os.path.join(TESTS_DIR, "*.in")))
    if not test_files:
        print(f"No .in files found in {TESTS_DIR}/")
        sys.exit(1)

    # Table header
    print(f"\n{'Test':<45}  {'Expected':>10}  {'Got':>10}  {'Time(s)':>8}  Status")
    print("-" * 90)

    total = passed = wa = tle = re_count = 0
    wa_tests = []
    tle_tests = []

    for in_path in test_files:
        out_path = in_path.replace(".in", ".out")
        name = os.path.basename(in_path).replace(".in", "")
        total += 1

        if not os.path.isfile(out_path):
            expected = "???"
        else:
            with open(out_path) as f:
                expected = f.read().strip()

        stdout, status, elapsed = run_one(cmd, in_path, effective_limit)

        if status == "TLE":
            result_str = "TLE"
            tle += 1
            tle_tests.append(name)
            got = "---"
        elif status.startswith("RE"):
            result_str = status
            re_count += 1
            got = "---"
        else:
            got = stdout if stdout is not None else ""
            if expected == "???":
                result_str = "SKIP(no .out)"
            elif got == expected:
                result_str = "PASS"
                passed += 1
            else:
                result_str = "WA"
                wa += 1
                wa_tests.append(name)

        print(f"{name:<45}  {expected:>10}  {got:>10}  {elapsed:>8.3f}  {result_str}")

    print("-" * 90)
    print(f"\nResults: {total} tests — "
          f"\033[32m{passed} PASS\033[0m, "
          f"\033[31m{wa} WA\033[0m, "
          f"\033[33m{tle} TLE\033[0m, "
          f"\033[35m{re_count} RE\033[0m")
    if wa_tests:
        print(f"  WA on: {', '.join(wa_tests)}")
    if tle_tests:
        print(f"  TLE on: {', '.join(tle_tests)}")

    if exe_cleanup and os.path.isfile(exe_cleanup):
        os.remove(exe_cleanup)

    print()


if __name__ == "__main__":
    main()
