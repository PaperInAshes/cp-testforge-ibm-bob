"""
gen.py — Test generator for Longest Increasing Subsequence problem.
Generates tests/ folder with categorized test cases.
Fixed seed for reproducibility.

Test categories:
  SAMPLE        — same as problem statement example
  MINIMAL       — smallest possible input
  BOUNDARY      — N at/near max, extreme values
  EDGE          — special array structures
  ANTI-WA       — catches common wrong answer bugs
  ANTI-OVERFLOW — values near ±1e9 (relevant for C++)
  MAX/STRESS    — N=100000 for TLE detection
  RANDOM-SMALL  — small random arrays
"""
import os
import random

SEED = 42
random.seed(SEED)

OUT_DIR = os.path.join(os.path.dirname(__file__), "tests")
os.makedirs(OUT_DIR, exist_ok=True)


def write_test(name, n, arr):
    path = os.path.join(OUT_DIR, f"{name}.in")
    with open(path, "w") as f:
        f.write(f"{n}\n")
        f.write(" ".join(map(str, arr)) + "\n")
    return path


# ── 01: SAMPLE ─────────────────────────────────────────────────────────────────
# Matches problem statement example; answer = 3
write_test("test_01_sample", 6, [5, 2, 8, 6, 3, 7])

# ── 02: MINIMAL — N=1 ──────────────────────────────────────────────────────────
# N=1 → LIS = 1; catches solusi yang return 0 saat N=1
write_test("test_02_minimal_n1", 1, [0])

# ── 03: MINIMAL — N=2, strictly increasing ─────────────────────────────────────
write_test("test_03_minimal_n2_inc", 2, [1, 2])

# ── 04: MINIMAL — N=2, decreasing ──────────────────────────────────────────────
write_test("test_04_minimal_n2_dec", 2, [2, 1])

# ── 05: EDGE — single long strictly increasing run ─────────────────────────────
# Array 1,2,3,...,1000 → LIS = 1000
# Catches off-by-one / early return bugs
n5 = 1000
write_test("test_05_edge_single_increase", n5, list(range(1, n5 + 1)))

# ── 06: EDGE — strictly decreasing ─────────────────────────────────────────────
# LIS = 1 (only single elements)
n6 = 500
write_test("test_06_edge_decreasing", n6, list(range(n6, 0, -1)))

# ── 07: EDGE — all equal elements ──────────────────────────────────────────────
# LIS = 1; catches bisect_right bug (wrong.py gives n7 here)
n7 = 1000
write_test("test_07_edge_all_equal", n7, [7] * n7)

# ── 08: EDGE — almost sorted (one element out of place) ────────────────────────
# [1,2,3,...,499, 1000, 500,...,999] → LIS still = 500 (first 499 + 1000)
# Actually let's craft: [1,2,...,498, 999, 499, 500,...,998] → LIS=499
base8 = list(range(1, 499)) + [999] + list(range(499, 999))
write_test("test_08_edge_almost_sorted", len(base8), base8)

# ── 09: ANTI-WA — array with negative values ───────────────────────────────────
# LIS crosses zero: [-5, -3, -1, 0, 2, 4] → LIS = 6
# Catches solutions that mis-handle negative numbers
arr9 = [-5, -3, -1, 0, 2, 4]
write_test("test_09_anti_wa_negative", len(arr9), arr9)

# ── 10: ANTI-WA — non-strict trap with mixed duplicates ────────────────────────
# [3, 1, 1, 2, 3] → strictly: LIS = [1,2,3]=3; non-strictly: 4 or 5
# wrong.py (bisect_right) gives 4
arr10 = [3, 1, 1, 2, 3]
write_test("test_10_anti_wa_non_strict", len(arr10), arr10)

# ── 11: ANTI-OVERFLOW — values near ±1e9 ───────────────────────────────────────
# Difference between max and min = 2e9 > INT_MAX (relevant for C++ int)
# LIS = 3: [-1000000000, 0, 1000000000]
arr11 = [-1_000_000_000, 500_000_000, -500_000_000, 0, 1_000_000_000, 999_999_999]
write_test("test_11_anti_overflow", len(arr11), arr11)

# ── 12: MAX/STRESS — N=100000, worst case for O(N^2): sorted array ──────────────
# Sorted ascending → LIS = N → forces full O(N log N) work
n12 = 100_000
arr12 = list(range(1, n12 + 1))
write_test("test_12_stress_max_sorted", n12, arr12)

# ── 13: MAX/STRESS — N=100000, all same (worst for wrong.py bisect_right) ──────
n13 = 100_000
arr13 = [42] * n13
write_test("test_13_stress_max_equal", n13, arr13)

# ── 14: MAX/STRESS — N=100000, random permutation ──────────────────────────────
n14 = 100_000
arr14 = list(range(1, n14 + 1))
random.shuffle(arr14)
write_test("test_14_stress_max_random", n14, arr14)

# ── 15: BOUNDARY — extreme negative values, strictly increasing ─────────────────
# All near -1e9, carefully spaced
arr15 = [-1_000_000_000 + i for i in range(200)]
write_test("test_15_boundary_neg_inc", len(arr15), arr15)

# ── 16: RANDOM-SMALL — small random 1 ──────────────────────────────────────────
n16 = 20
arr16 = [random.randint(-50, 50) for _ in range(n16)]
write_test("test_16_random_small_1", n16, arr16)

# ── 17: RANDOM-SMALL — small random 2 ──────────────────────────────────────────
n17 = 30
arr17 = [random.randint(-100, 100) for _ in range(n17)]
write_test("test_17_random_small_2", n17, arr17)

# ── 18: EDGE — zigzag pattern ──────────────────────────────────────────────────
# 1,100,2,99,3,98,... → LIS = 50 (every odd position)
# Tests that algo correctly ignores non-relevant elements
n18 = 100
arr18 = []
for i in range(n18 // 2):
    arr18.append(i + 1)
    arr18.append(1000 - i)
write_test("test_18_edge_zigzag", len(arr18), arr18)

# ── 19: ANTI-WA — single element repeated then one larger ─────────────────────
# [5,5,5,5,6] → strictly: LIS = [5,6] = 2; non-strictly: 5
arr19 = [5] * 10 + [6]
write_test("test_19_anti_wa_dup_then_larger", len(arr19), arr19)

# ── 20: MAX/STRESS — N=100000, reverse sorted (each LIS=1) ─────────────────────
n20 = 100_000
arr20 = list(range(n20, 0, -1))
write_test("test_20_stress_max_reverse", n20, arr20)

print(f"Generated {len(os.listdir(OUT_DIR))} test files in {OUT_DIR}/")
