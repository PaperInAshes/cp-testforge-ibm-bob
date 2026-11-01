"""
cross_verify.py — Run 200 random small tests and compare brute vs sol.
Prints a summary at the end.
"""
import random
import subprocess
import sys

SEED = 1234
random.seed(SEED)

N_TESTS = 200
MAX_N = 50
MIN_VAL = -100
MAX_VAL = 100

mismatches = 0

for t in range(N_TESTS):
    n = random.randint(1, MAX_N)
    arr = [random.randint(MIN_VAL, MAX_VAL) for _ in range(n)]
    inp = f"{n}\n{' '.join(map(str, arr))}\n"

    r_brute = subprocess.run(
        [sys.executable, "brute.py"],
        input=inp, capture_output=True, text=True, timeout=10
    )
    r_sol = subprocess.run(
        [sys.executable, "sol.py"],
        input=inp, capture_output=True, text=True, timeout=10
    )

    b_out = r_brute.stdout.strip()
    s_out = r_sol.stdout.strip()

    if b_out != s_out:
        mismatches += 1
        print(f"MISMATCH test {t+1}: n={n} arr={arr}")
        print(f"  brute={b_out}  sol={s_out}")

if mismatches == 0:
    print(f"All {N_TESTS} random small tests: brute == sol ✓")
else:
    print(f"{mismatches} MISMATCHES found in {N_TESTS} tests!")
    sys.exit(1)
