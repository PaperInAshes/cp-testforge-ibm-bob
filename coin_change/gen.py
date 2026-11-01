"""
gen.py — Test case generator for Coin Change.
Generates tests/ folder with categorized test cases.
Seed fixed for reproducibility.

Categories:
  SAMPLE         — from problem statement
  MINIMAL        — smallest possible N and X
  BOUNDARY       — max/min boundary values
  EDGE           — structural edge cases (all coins > X, single coin = X, etc.)
  ANTI-WA        — anti-wrong-answer (defeats greedy)
  ANTI-OVERFLOW  — large values that might cause integer overflow in C
  MAX/STRESS     — maximum constraints
  RANDOM-SMALL   — small random inputs
"""
import random
import os

SEED = 42
random.seed(SEED)

TESTS_DIR = os.path.join(os.path.dirname(__file__), "tests")
os.makedirs(TESTS_DIR, exist_ok=True)

tests = []  # list of (filename_prefix, N, X, coins, category, trap_description)

# ─────────────────────────────────────────────
# 01 SAMPLE — from problem statement
# Trap: baseline correctness
# ─────────────────────────────────────────────
tests.append(("01_sample", 3, 11, [1, 2, 5],
              "SAMPLE", "Baseline — contoh dari soal (expected: 3)"))

# ─────────────────────────────────────────────
# 02 MINIMAL — N=1, X=1, C=[1]
# Trap: N=1 minimum, smallest possible case
# ─────────────────────────────────────────────
tests.append(("02_minimal_possible", 1, 1, [1],
              "MINIMAL", "N=1, X=1, C=[1] — paling kecil (expected: 1)"))

# ─────────────────────────────────────────────
# 03 MINIMAL IMPOSSIBLE — N=1, X=3, C=[2]
# Trap 2: impossible case (no 1-coin), must return -1
# ─────────────────────────────────────────────
tests.append(("03_minimal_impossible", 1, 3, [2],
              "MINIMAL", "N=1, X=3, C=[2] — mustahil (expected: -1) [Jebakan 2]"))

# ─────────────────────────────────────────────
# 04 EDGE — All coins > X → impossible
# Trap 4: coins all larger than X
# ─────────────────────────────────────────────
tests.append(("04_edge_all_coins_gt_x", 3, 2, [5, 7, 10],
              "EDGE", "Semua koin > X, mustahil (expected: -1) [Jebakan 4]"))

# ─────────────────────────────────────────────
# 05 EDGE — Exactly one coin equals X
# Trap 6: single coin = X → answer is 1
# ─────────────────────────────────────────────
tests.append(("05_edge_coin_equals_x", 3, 5, [3, 5, 8],
              "EDGE", "Satu koin tepat = X (expected: 1) [Jebakan 6]"))

# ─────────────────────────────────────────────
# 06 ANTI-WA — Greedy fails (non-canonical coins)
# Trap 1: greedy picks 4+1+1=3, optimal is 3+3=2
# X=6, coins={1,3,4}
# ─────────────────────────────────────────────
tests.append(("06_anti_wa_greedy_fail_1", 3, 6, [1, 3, 4],
              "ANTI-WA", "Greedy ambil 4+1+1=3 koin, optimal 3+3=2 [Jebakan 1]"))

# ─────────────────────────────────────────────
# 07 ANTI-WA — Greedy fails (stronger case)
# X=30, coins={1,5,6,9} — greedy: 9+9+9+3... optimal uses different combo
# greedy: 9+9+9+3 → 9+9+9 leaves 3, needs 3×1 → 6 coins
# optimal: 9+9+6+6=30 → 4 coins
# ─────────────────────────────────────────────
tests.append(("07_anti_wa_greedy_fail_2", 4, 30, [1, 5, 6, 9],
              "ANTI-WA", "Greedy gagal kuat: X=30, koin={1,5,6,9} (expected: 4) [Jebakan 1]"))

# ─────────────────────────────────────────────
# 08 ANTI-WA — Bounded vs Unbounded
# Trap 5: needs same coin multiple times: X=4, coins=[2]
# bounded (0/1) would say -1, unbounded says 2
# ─────────────────────────────────────────────
tests.append(("08_anti_wa_unbounded", 1, 4, [2],
              "ANTI-WA", "Butuh koin sama 2x: X=4, koin=[2] (expected: 2) [Jebakan 5]"))

# ─────────────────────────────────────────────
# 09 BOUNDARY — X=10000 with coin=1 (max X, always possible)
# Trap 7 (anti-TLE for slow): X=10000, answer=10000
# Also tests slow.py TLE
# ─────────────────────────────────────────────
tests.append(("09_boundary_max_x_coin1", 1, 10000, [1],
              "MAX/STRESS", "X maksimum dengan koin=1 (expected: 10000) [Jebakan 7 TLE]"))

# ─────────────────────────────────────────────
# 10 MAX/STRESS — N=100, X=10000, diverse coins
# Maximum constraints stress test
# ─────────────────────────────────────────────
random.seed(SEED + 1)
big_coins = random.sample(range(1, 10001), 100)
tests.append(("10_max_stress", 100, 10000, big_coins,
              "MAX/STRESS", "N=100, X=10000, 100 koin acak [Jebakan 7 TLE untuk slow]"))

# ─────────────────────────────────────────────
# 11 BOUNDARY — X=1, all coins >= 2 except one
# X=1, coins=[1,2,3] → must use the coin=1, answer=1
# ─────────────────────────────────────────────
tests.append(("11_boundary_x1", 3, 1, [1, 2, 3],
              "BOUNDARY", "X=1 (minimum X), hanya koin=1 yang bisa dipakai (expected: 1)"))

# ─────────────────────────────────────────────
# 12 ANTI-OVERFLOW — Large coin values, X large
# Tests for C int32 overflow: C[i]=9999, X=9999 → 1 coin
# Also: X=10000, C=[9999, 1] → 2 coins (9999+1)
# ─────────────────────────────────────────────
tests.append(("12_anti_overflow", 2, 10000, [9999, 1],
              "ANTI-OVERFLOW", "Nilai koin besar mendekati X: X=10000, koin={9999,1} (expected: 2)"))

# ─────────────────────────────────────────────
# 13 EDGE — Impossible with large non-trivial coins
# X=7, coins={3,5} — can't make 7 exactly (3+3=6≠7, 5+3=8≠7, 3+5=8)
# → -1
# ─────────────────────────────────────────────
tests.append(("13_edge_impossible_nontrivial", 2, 7, [3, 5],
              "EDGE", "Mustahil non-trivial: X=7, koin={3,5} (expected: -1) [Jebakan 2]"))

# ─────────────────────────────────────────────
# 14 RANDOM-SMALL — Random small input #1
# ─────────────────────────────────────────────
random.seed(SEED + 10)
rc1 = random.sample(range(1, 20), random.randint(3, 8))
rx1 = random.randint(5, 50)
tests.append(("14_random_small_1", len(rc1), rx1, rc1,
              "RANDOM-SMALL", f"Acak kecil #1: N={len(rc1)}, X={rx1}"))

# ─────────────────────────────────────────────
# 15 RANDOM-SMALL — Random small input #2
# ─────────────────────────────────────────────
random.seed(SEED + 20)
rc2 = random.sample(range(1, 30), random.randint(3, 8))
rx2 = random.randint(10, 80)
tests.append(("15_random_small_2", len(rc2), rx2, rc2,
              "RANDOM-SMALL", f"Acak kecil #2: N={len(rc2)}, X={rx2}"))

# ─────────────────────────────────────────────
# 16 ANTI-WA — DP init bug: dp[0] wrong
# X=2, coins=[2] → answer 1. If dp[0]=1 bug → answer 2
# ─────────────────────────────────────────────
tests.append(("16_anti_wa_dp_init", 1, 2, [2],
              "ANTI-WA", "X=2, koin=[2]: deteksi bug inisialisasi dp[0] (expected: 1) [Jebakan 3]"))

# ─────────────────────────────────────────────
# Write all test files
# ─────────────────────────────────────────────
for (prefix, N, X, coins, category, desc) in tests:
    fname = os.path.join(TESTS_DIR, prefix + ".in")
    with open(fname, 'w') as f:
        f.write(f"{N} {X}\n")
        f.write(" ".join(str(c) for c in coins) + "\n")
    print(f"  Written: {prefix}.in  [{category}] {desc}")

print(f"\nTotal: {len(tests)} test cases generated in {TESTS_DIR}/")
