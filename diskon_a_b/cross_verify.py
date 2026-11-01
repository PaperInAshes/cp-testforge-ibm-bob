#!/usr/bin/env python3
"""
cross_verify.py — run 200 random small tests comparing brute.py vs sol.cpp
"""
import random
import subprocess
import sys
import os

SOL_BIN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sol_bin")
BRUTE   = os.path.join(os.path.dirname(os.path.abspath(__file__)), "brute.py")

def run(cmd, inp):
    r = subprocess.run(cmd, input=inp, capture_output=True, text=True, timeout=5)
    return r.stdout.strip()

rng = random.Random(2024)
TRIALS = 200
mismatch = 0

for trial in range(TRIALS):
    N = rng.randint(1, 15)
    A = rng.randint(1, 10)
    B = rng.randint(1, 10)
    h = [rng.randint(1, 1000) for _ in range(N)]
    inp = f"{N} {A} {B}\n{' '.join(map(str, h))}\n"

    brute_ans = run([sys.executable, BRUTE], inp)
    sol_ans   = run([SOL_BIN], inp)

    if brute_ans != sol_ans:
        mismatch += 1
        print(f"MISMATCH trial {trial+1}: input={inp.strip()!r}")
        print(f"  brute={brute_ans!r}  sol={sol_ans!r}")

print(f"\nCross-verification: {TRIALS} trials, {mismatch} mismatches")
sys.exit(0 if mismatch == 0 else 1)
