#!/usr/bin/env python3
"""
run_tests.py — test runner for "Diskon Beli A Gratis B"
Usage: python3 run_tests.py <solution_file>

Supports:
  - .cpp files: compiled with g++ -O2
  - .py files: run directly with python3

Time limit: 1 second (from problem statement)
Reports PASS / WA / TLE / RE per test.
"""

import sys
import os
import subprocess
import tempfile
import shutil
import time

TESTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests")
TIME_LIMIT = 1.0  # seconds

RESET  = "\033[0m"
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"


def compile_cpp(src: str) -> str:
    """Compile a C++ file, return path to binary. Raises on error."""
    binary = tempfile.mktemp(suffix=".bin")
    result = subprocess.run(
        ["g++", "-O2", "-o", binary, src],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"Compilation failed:\n{result.stderr}")
    return binary


def run_solution(cmd: list, input_text: str, time_limit: float):
    """
    Run a command with given stdin, return (stdout, stderr, elapsed, status).
    status: 'ok' | 'tle' | 're'
    """
    start = time.perf_counter()
    try:
        proc = subprocess.run(
            cmd,
            input=input_text,
            capture_output=True,
            text=True,
            timeout=time_limit * 2  # give 2x time to detect TLE gracefully
        )
        elapsed = time.perf_counter() - start
        if proc.returncode != 0:
            return proc.stdout, proc.stderr, elapsed, 're'
        if elapsed > time_limit:
            return proc.stdout, proc.stderr, elapsed, 'tle'
        return proc.stdout, proc.stderr, elapsed, 'ok'
    except subprocess.TimeoutExpired:
        elapsed = time.perf_counter() - start
        return "", "", elapsed, 'tle'


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 run_tests.py <solution_file>", file=sys.stderr)
        sys.exit(1)

    sol_file = os.path.abspath(sys.argv[1])
    if not os.path.exists(sol_file):
        print(f"Error: file not found: {sol_file}", file=sys.stderr)
        sys.exit(1)

    ext = os.path.splitext(sol_file)[1].lower()
    binary = None

    print(f"{BOLD}Running tests for: {os.path.basename(sol_file)}{RESET}")
    print(f"Time limit: {TIME_LIMIT}s\n")

    if ext == '.cpp':
        print("Compiling...", end=" ", flush=True)
        try:
            binary = compile_cpp(sol_file)
            print(f"{GREEN}OK{RESET}")
        except RuntimeError as e:
            print(f"{RED}FAILED{RESET}")
            print(e)
            sys.exit(1)
        cmd_base = [binary]
    elif ext == '.py':
        cmd_base = [sys.executable, sol_file]
    else:
        print(f"Unsupported extension: {ext}", file=sys.stderr)
        sys.exit(1)

    # Gather tests
    test_files = sorted(
        f for f in os.listdir(TESTS_DIR) if f.endswith('.in')
    )
    if not test_files:
        print("No test files found in tests/", file=sys.stderr)
        sys.exit(1)

    results = []
    pass_count = wa_count = tle_count = re_count = 0

    for fname in test_files:
        base = fname[:-3]
        in_path  = os.path.join(TESTS_DIR, fname)
        out_path = os.path.join(TESTS_DIR, base + ".out")

        with open(in_path) as f:
            input_text = f.read()

        expected = None
        if os.path.exists(out_path):
            with open(out_path) as f:
                expected = f.read().strip()

        stdout, stderr, elapsed, status = run_solution(cmd_base, input_text, TIME_LIMIT)

        if status == 'tle':
            label = f"{RED}TLE{RESET}"
            tle_count += 1
        elif status == 're':
            label = f"{RED}RE{RESET}"
            re_count += 1
        elif expected is None:
            label = f"{YELLOW}NOEXP{RESET}"
            pass_count += 1
        elif stdout.strip() == expected:
            label = f"{GREEN}PASS{RESET}"
            pass_count += 1
        else:
            label = f"{RED}WA{RESET}"
            wa_count += 1

        time_str = f"{elapsed:.3f}s"
        if elapsed > TIME_LIMIT:
            time_str = f"{RED}{time_str}{RESET}"

        results.append((base, label, time_str, stdout.strip(), expected))
        status_plain = label.replace(RESET,'').replace(GREEN,'').replace(RED,'').replace(YELLOW,'').replace(CYAN,'').replace(BOLD,'')
        print(f"  {base}: {label}  ({time_str})", end="")
        if 'WA' in status_plain:
            print(f"  expected={repr(expected)}  got={repr(stdout.strip())}", end="")
        elif 'RE' in status_plain and stderr:
            print(f"  stderr={repr(stderr[:80])}", end="")
        print()

    print()
    print(f"{BOLD}Summary:{RESET} {pass_count} PASS / {wa_count} WA / {tle_count} TLE / {re_count} RE  (total {len(test_files)})")

    # Cleanup
    if binary and os.path.exists(binary):
        os.unlink(binary)

    if wa_count + tle_count + re_count > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
