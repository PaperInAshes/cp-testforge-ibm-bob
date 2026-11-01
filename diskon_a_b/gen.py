#!/usr/bin/env python3
"""
gen.py — test generator for "Diskon Beli A Gratis B"
Generates folder tests/ with at least 14 test cases.
All seeds are fixed for reproducibility.

Usage: python3 gen.py
"""
import random
import os
import sys

TESTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests")
os.makedirs(TESTS_DIR, exist_ok=True)

def write_test(num: int, N: int, A: int, B: int, h: list, label: str = ""):
    fname = f"{num:02d}"
    in_path = os.path.join(TESTS_DIR, f"{fname}.in")
    with open(in_path, 'w') as f:
        f.write(f"{N} {A} {B}\n")
        f.write(" ".join(map(str, h)) + "\n")
    tag = f" [{label}]" if label else ""
    print(f"  test {fname}: N={N} A={A} B={B}{tag}")
    return in_path


tests = []
t = 0

# ── Sample tests (must match problem statement exactly) ──────────────────────

t += 1
# Sample 1: N=5 A=2 B=1, answer=270
tests.append(write_test(t, 5, 2, 1, [60, 100, 30, 75, 80], "sample1"))

t += 1
# Sample 2: N=4 A=2 B=3, N < A+B so no groups, pay all
tests.append(write_test(t, 4, 2, 3, [100, 50, 70, 30], "sample2_no_group"))

# ── Minimal / boundary tests ─────────────────────────────────────────────────

t += 1
# N=1 A=1 B=1: single item, cannot form group (need 2), pay full
tests.append(write_test(t, 1, 1, 1, [999999999], "N1_no_group"))

t += 1
# N=A+B exactly one group, B=1 (classic buy-2-get-1-free)
tests.append(write_test(t, 3, 2, 1, [100, 70, 30], "exact_one_group"))

t += 1
# N=A+B exactly one group, B=B (all B items free)
tests.append(write_test(t, 5, 2, 3, [90, 80, 70, 60, 50], "exact_one_group_B3"))

t += 1
# A=1 B=1: buy-1-get-1-free, every other item free
# N=6: items [100,90,80,70,60,50], groups=3, free: indices 1,3,5
tests.append(write_test(t, 6, 1, 1, [100, 90, 80, 70, 60, 50], "buy1get1free"))

t += 1
# N = A+B - 1: one item short of a full group, no discount at all
# Trap: wrong_offbyone might still skip one item
N7, A7, B7 = 4, 2, 3   # need 5 for a group, only 4
tests.append(write_test(t, N7, A7, B7, [1000000000, 900000000, 800000000, 700000000],
                         "one_short_of_group"))

t += 1
# All items identical: discount still applies, B items per group freed
# N=9 A=2 B=1: 3 groups, 3 items freed, total=6*500
tests.append(write_test(t, 9, 2, 1, [500]*9, "all_equal"))

# ── Overflow trap ─────────────────────────────────────────────────────────────

t += 1
# Large N, large h: total can exceed 2^31-1 (~2.1e9)
# N=100000, A=1, B=1, all h=1e9 → ~50000 items paid × 1e9 = 5e13 (overflows int32)
rng = random.Random(42)
N9 = 100000
h9 = [1_000_000_000] * N9
tests.append(write_test(t, N9, 1, 1, h9, "overflow_large_sum"))

# ── Greedy order trap ────────────────────────────────────────────────────────

t += 1
# Items with large spread: must free expensive, not cheap ones
# Wrong ascending sort would free the cheapest (small) items → bigger total
# N=6 A=2 B=1: sorted desc [1000,999,1,1,1,1]
# correct: groups=2, free indices 2,5 → free h[2]=1 and h[5]=1
# wrong_greedy_order (ascending sort): free h[2] and h[5] which are the bigger ones
tests.append(write_test(t, 6, 2, 1,
             [1, 1, 1, 1, 999, 1000],
             "greedy_order_spread"))

t += 1
# Greedy order: multiple groups, free items are clearly the most expensive ones
# N=9 A=1 B=2: step=3, groups=3, free indices 1,2,4,5,7,8
# Sorted desc: [900,800,700,600,500,400,300,200,100]
# Correct free: 800,700,500,400,200,100 → pay 900+600+300=1800
# Wrong ascending: free 100,200,300,400,500,600 → pay 900+800+700=2400
tests.append(write_test(t, 9, 1, 2,
             [900, 800, 700, 600, 500, 400, 300, 200, 100],
             "greedy_order_A1B2"))

# ── Off-by-one trap ──────────────────────────────────────────────────────────

t += 1
# A=1 B=2: step=3. wrong_offbyone frees idx > 1 (i.e., only idx 2), missing idx 1
# N=3: correct frees 2 items (indices 1 and 2 in group), wrong frees only 1
# N=6: correct frees 4 items, wrong frees only 2
tests.append(write_test(t, 6, 1, 2,
             [300, 200, 100, 300, 200, 100],
             "offbyone_A1B2"))

t += 1
# B=3: step=A+B=5. Correct: free idx 2,3,4 per group. wrong_offbyone: free idx 3,4 only
# N=10 A=2 B=3: 2 groups, each frees 3 correct vs 2 wrong
rng2 = random.Random(100)
h13 = sorted([rng2.randint(1, 1000) for _ in range(10)], reverse=True)
tests.append(write_test(t, 10, 2, 3, h13, "offbyone_B3"))

# ── Large test for TLE ───────────────────────────────────────────────────────

t += 1
# Maximum N, A, B, random values — slow.cpp O(N*A) will TLE
rng3 = random.Random(7)
N14 = 100000
A14 = 50000  # large A makes O(N*A) very slow
B14 = 1
h14 = [rng3.randint(1, 1_000_000_000) for _ in range(N14)]
tests.append(write_test(t, N14, A14, B14, h14, "large_TLE_bigA"))

t += 1
# Another large test: A=B=50000 (maximum step, maximum inner loop for slow.cpp)
rng4 = random.Random(13)
N15 = 100000
A15 = 50000
B15 = 50000
h15 = [rng4.randint(1, 1_000_000_000) for _ in range(N15)]
tests.append(write_test(t, N15, A15, B15, h15, "large_TLE_maxAB"))

t += 1
# Large N with A=1 B=99999 (only one item per group is paid, rest free)
# Tests correct group counting for extreme B
rng5 = random.Random(99)
N16 = 100000
A16 = 1
B16 = 99999
h16 = [rng5.randint(1, 1_000_000_000) for _ in range(N16)]
tests.append(write_test(t, N16, A16, B16, h16, "large_A1_maxB"))

t += 1
# Many groups: N=100000, A=2, B=1 (step=3) → 33333 groups, 33333 free items
# Ensures correct group-count floor division
rng6 = random.Random(55)
N17 = 100000
h17 = sorted([rng6.randint(1, 1_000_000_000) for _ in range(N17)], reverse=True)
tests.append(write_test(t, N17, 2, 1, h17, "large_many_groups"))

t += 1
# N = A+B (exactly one group), large values, overflow check
# A=99999 B=1: step=100000=N, one group, only last item (cheapest) free
rng7 = random.Random(77)
N18 = 100000
A18 = 99999
B18 = 1
h18 = sorted([rng7.randint(500_000_000, 1_000_000_000) for _ in range(N18)], reverse=True)
tests.append(write_test(t, N18, A18, B18, h18, "exact_one_group_large"))

print(f"\nGenerated {t} tests in {TESTS_DIR}/")
