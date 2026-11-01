#!/usr/bin/env python3
"""
cross_verify.py - Verifikasi silang brute.py vs sol.py pada 200 test acak kecil.
"""
import random
import subprocess
import sys
import os

SEED = 12345
rng = random.Random(SEED)

BASE = os.path.dirname(__file__)
BRUTE = os.path.join(BASE, "brute.py")
SOL = os.path.join(BASE, "sol.py")

def make_random_graph(N_max=20, M_max=40):
    N = rng.randint(2, N_max)
    M = rng.randint(1, M_max)
    lines = [f"{N} {M}"]
    for _ in range(M):
        u = rng.randint(1, N)
        v = rng.randint(1, N)
        w = rng.randint(1, 1_000_000_000)
        lines.append(f"{u} {v} {w}")
    return '\n'.join(lines) + '\n', N

def run(script, input_data):
    result = subprocess.run(
        ['python3', script],
        input=input_data.encode(),
        capture_output=True,
        timeout=10
    )
    return result.stdout.decode().strip()

errors = 0
total = 200
print(f"Cross-verifying brute.py vs sol.py on {total} random small tests...")

for i in range(1, total + 1):
    inp, N = make_random_graph()
    try:
        brute_out = run(BRUTE, inp)
        sol_out = run(SOL, inp)
    except subprocess.TimeoutExpired:
        print(f"  Test {i}: TIMEOUT")
        errors += 1
        continue

    if brute_out != sol_out:
        print(f"  Test {i}: MISMATCH! brute={brute_out}, sol={sol_out}")
        print(f"  Input: {inp[:200]}")
        errors += 1
    elif i % 50 == 0:
        print(f"  Test {i}: OK (brute={brute_out}, sol={sol_out})")

print(f"\nResult: {total - errors}/{total} passed, {errors} mismatches")
if errors == 0:
    print("CROSS-VERIFY: LULUS semua 200 test!")
    sys.exit(0)
else:
    print("CROSS-VERIFY: ADA MISMATCH!")
    sys.exit(1)
