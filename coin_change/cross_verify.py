"""
cross_verify.py — Cross-verify brute.py vs sol.py on 200 random small inputs.
"""
import random
import subprocess
import sys

SEED = 999
random.seed(SEED)

PASS = 0
FAIL = 0
errors = []

def run(script, input_str):
    result = subprocess.run(
        [sys.executable, script],
        input=input_str, capture_output=True, text=True, timeout=10
    )
    return result.stdout.strip()

for i in range(200):
    N = random.randint(1, 10)
    X = random.randint(1, 100)
    coins = random.sample(range(1, 50), min(N, 49))
    N = len(coins)
    inp = f"{N} {X}\n{' '.join(map(str, coins))}\n"
    
    b = run("brute.py", inp)
    s = run("sol.py", inp)
    
    if b == s:
        PASS += 1
    else:
        FAIL += 1
        errors.append((i+1, inp.strip(), b, s))

print(f"Cross-verify: {PASS}/200 PASS, {FAIL}/200 FAIL")
if errors:
    print("\nFailed cases:")
    for idx, inp, b, s in errors[:5]:
        print(f"  Case {idx}: input={inp!r}  brute={b}  sol={s}")
else:
    print("All 200 random small tests: brute == sol ✓")
