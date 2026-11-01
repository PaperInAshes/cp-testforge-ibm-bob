"""
run_tests.py  –  Run a solution against all tests/*.in and report results.
Usage: python3 run_tests.py <solution.py> [--tl SECONDS]
Reports PASS / FAIL / TLE per test, then a summary.
Exit code 0 if all pass, else 1.
"""
import subprocess
import sys
import os
import time
import glob

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 run_tests.py <solution.py> [--tl SECONDS]")
        sys.exit(1)

    solution = sys.argv[1]
    tl = 1.0  # default time limit in seconds

    # Parse optional --tl flag
    args = sys.argv[2:]
    if '--tl' in args:
        idx = args.index('--tl')
        tl = float(args[idx + 1])

    test_inputs = sorted(glob.glob(os.path.join("tests", "*.in")))
    if not test_inputs:
        print("No test files found in tests/")
        sys.exit(1)

    PASS = FAIL = TLE = 0
    results = []

    print(f"\nRunning {solution} against {len(test_inputs)} tests  (TL={tl}s)\n")
    print(f"{'Test':<35} {'N':>7}  {'Time':>8}  Status")
    print("-" * 65)

    for inp_path in test_inputs:
        out_path = inp_path.replace(".in", ".out")
        test_name = os.path.basename(inp_path)

        with open(inp_path) as f:
            N = int(f.readline().strip())

        # Read expected output
        if not os.path.exists(out_path):
            print(f"{test_name:<35} {'N='+str(N):>7}  {'':>8}  SKIP (no .out)")
            continue

        with open(out_path) as f:
            expected = f.read().strip()

        with open(inp_path) as f:
            inp_data = f.read()

        start = time.perf_counter()
        try:
            proc = subprocess.run(
                ["python3", solution],
                input=inp_data,
                capture_output=True,
                text=True,
                timeout=tl * 3  # allow 3× TL before hard kill
            )
            elapsed = time.perf_counter() - start
            actual = proc.stdout.strip()

            if elapsed > tl:
                status = "TLE"
                TLE += 1
            elif actual == expected:
                status = "PASS"
                PASS += 1
            else:
                status = f"FAIL  (got={actual!r}, want={expected!r})"
                FAIL += 1
        except subprocess.TimeoutExpired:
            elapsed = tl * 3
            status = "TLE (hard kill)"
            TLE += 1

        print(f"{test_name:<35} {'N='+str(N):>7}  {elapsed:>7.3f}s  {status}")
        results.append((test_name, status))

    print("-" * 65)
    print(f"\nSummary: {PASS} PASS  {FAIL} FAIL  {TLE} TLE  (total {PASS+FAIL+TLE})\n")

    sys.exit(0 if (FAIL == 0 and TLE == 0) else 1)

if __name__ == '__main__':
    main()
