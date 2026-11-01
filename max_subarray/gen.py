"""
gen.py  –  Test generator for Maximum Subarray Sum
Generates tests/ folder with labeled .in files.
Seed is fixed for reproducibility.
Usage: python gen.py
"""
import random
import os

SEED = 42
rng = random.Random(SEED)

OUT_DIR = os.path.join(os.path.dirname(__file__), "tests")
os.makedirs(OUT_DIR, exist_ok=True)

def write_test(name, N, arr):
    path = os.path.join(OUT_DIR, name + ".in")
    with open(path, "w") as f:
        f.write(f"{N}\n")
        f.write(" ".join(map(str, arr)) + "\n")
    return path

tests = []  # list of (name, category, N, note)

# ── 01  SAMPLE ────────────────────────────────────────────────────────────────
name = "01_sample"
arr  = [1, -2, 3, 4, -1]
write_test(name, len(arr), arr)
tests.append((name, "SAMPLE", len(arr), "Contoh dari soal; answer=7"))

# ── 02  MINIMAL  N=1  positive ────────────────────────────────────────────────
name = "02_minimal_pos"
arr  = [999999999]
write_test(name, 1, arr)
tests.append((name, "MINIMAL", 1, "N=1 positif"))

# ── 03  MINIMAL  N=1  negative ────────────────────────────────────────────────
name = "03_minimal_neg"
arr  = [-1]
write_test(name, 1, arr)
tests.append((name, "MINIMAL", 1, "N=1 negatif; answer=-1"))

# ── 04  BOUNDARY  nilai tepat -10^9 dan +10^9 ────────────────────────────────
name = "04_boundary"
arr  = [-10**9, 10**9, -10**9, 10**9]
write_test(name, len(arr), arr)
tests.append((name, "BOUNDARY", len(arr), "nilai tepat ±1e9"))

# ── 05  EDGE  semua negatif ───────────────────────────────────────────────────
name = "05_all_negative"
N    = 10
arr  = [-rng.randint(1, 10**9) for _ in range(N)]
write_test(name, N, arr)
tests.append((name, "EDGE", N, "semua negatif; answer = max element"))

# ── 06  EDGE  semua nol ───────────────────────────────────────────────────────
name = "06_all_zero"
N    = 8
arr  = [0] * N
write_test(name, N, arr)
tests.append((name, "EDGE", N, "semua nol; answer=0"))

# ── 07  EDGE  semua elemen sama (positif) ────────────────────────────────────
name = "07_all_same_pos"
N    = 6
arr  = [5] * N
write_test(name, N, arr)
tests.append((name, "EDGE", N, "semua sama positif; answer=30"))

# ── 08  ANTI-WRONG-ANSWER  menjebak inisialisasi max=0 ───────────────────────
# Array semua negatif: solusi salah akan mengembalikan 0, bukan max elemen
name = "08_anti_wrong_all_neg"
arr  = [-3, -1, -4, -1, -5, -9, -2, -6]
write_test(name, len(arr), arr)
tests.append((name, "ANTI-WRONG-ANSWER", len(arr),
              "semua negatif → inisialisasi max=0 menghasilkan 0 (salah)"))

# ── 09  ANTI-WRONG-ANSWER  prefix besar, lalu turun, semua elemen < 0 di akhir
name = "09_anti_wrong_prefix"
# Best subarray adalah elemen pertama saja (-1), tapi setelah itu semua << 0
arr  = [-1, -10, -10, -10, -10]
write_test(name, len(arr), arr)
tests.append((name, "ANTI-WRONG-ANSWER", len(arr),
              "seluruh array negatif; max=0 akan salah"))

# ── 10  ANTI-OVERFLOW  N=100000 semua 10^9 ───────────────────────────────────
# Jawaban = 100000 * 1e9 = 1e14, melebihi 32-bit integer
name = "10_anti_overflow"
N    = 100_000
arr  = [10**9] * N
write_test(name, N, arr)
tests.append((name, "ANTI-OVERFLOW", N,
              "N=100000 semua 1e9; answer=1e14, perlu 64-bit"))

# ── 11  MAX/STRESS  N=100000 acak ────────────────────────────────────────────
name = "11_stress_random"
N    = 100_000
arr  = [rng.randint(-10**9, 10**9) for _ in range(N)]
write_test(name, N, arr)
tests.append((name, "MAX/STRESS", N, "N=100000 acak campuran"))

# ── 12  MAX/STRESS  N=100000 mixed negatif berat ─────────────────────────────
name = "12_stress_heavy_neg"
N    = 100_000
# 90% negatif besar, 10% positif kecil
arr  = []
for _ in range(N):
    if rng.random() < 0.1:
        arr.append(rng.randint(1, 1000))
    else:
        arr.append(rng.randint(-10**9, -1))
write_test(name, N, arr)
tests.append((name, "MAX/STRESS", N, "N=100000, 90% negatif besar"))

# ── 13  RANDOM KECIL  1 ───────────────────────────────────────────────────────
name = "13_small_random_1"
N    = rng.randint(2, 20)
arr  = [rng.randint(-100, 100) for _ in range(N)]
write_test(name, N, arr)
tests.append((name, "RANDOM-SMALL", N, "acak kecil #1"))

# ── 14  RANDOM KECIL  2 ───────────────────────────────────────────────────────
name = "14_small_random_2"
N    = rng.randint(2, 20)
arr  = [rng.randint(-100, 100) for _ in range(N)]
write_test(name, N, arr)
tests.append((name, "RANDOM-SMALL", N, "acak kecil #2"))

# ── 15  RANDOM KECIL  3 ───────────────────────────────────────────────────────
name = "15_small_random_3"
N    = rng.randint(2, 20)
arr  = [rng.randint(-100, 100) for _ in range(N)]
write_test(name, N, arr)
tests.append((name, "RANDOM-SMALL", N, "acak kecil #3"))

# ── Ringkasan ─────────────────────────────────────────────────────────────────
print(f"Generated {len(tests)} tests in {OUT_DIR}/")
for name, cat, n, note in tests:
    print(f"  {name}.in  [{cat}]  N={n}  — {note}")
