"""
crosscheck.py  –  Run 200 random small tests, compare brute.py vs sol.py.
Prints a summary and exits with code 1 if any mismatch found.
"""
import random
import subprocess
import sys

SEED = 2024
rng  = random.Random(SEED)
TRIALS = 200
MISMATCHES = 0

for trial in range(1, TRIALS + 1):
    N   = rng.randint(1, 50)
    arr = [rng.randint(-10**6, 10**6) for _ in range(N)]
    inp = f"{N}\n{' '.join(map(str, arr))}\n"

    brute_out = subprocess.run(
        ["python3", "brute.py"], input=inp, capture_output=True, text=True
    ).stdout.strip()

    sol_out = subprocess.run(
        ["python3", "sol.py"], input=inp, capture_output=True, text=True
    ).stdout.strip()

    if brute_out != sol_out:
        MISMATCHES += 1
        print(f"MISMATCH on trial {trial}: brute={brute_out}  sol={sol_out}")
        print(f"  Input: {inp.strip()}")

if MISMATCHES == 0:
    print(f"crosscheck: {TRIALS}/{TRIALS} trials matched — brute.py and sol.py agree on all tests.")
else:
    print(f"crosscheck: {MISMATCHES} MISMATCH(es) found in {TRIALS} trials!")
    sys.exit(1)
