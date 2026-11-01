#!/usr/bin/env python3
"""
gen.py — Generator test case untuk soal Penukaran Emas.
Menghasilkan folder tests/ berisi minimal 12 test case dengan kategori beragam.
Seed tetap untuk reproducibility.
"""
import os
import random

SEED = 42
random.seed(SEED)

OUTPUT_DIR = "tests"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==============================================================================
# Definisi semua test case
# Format: (filename_prefix, category, N_value, description)
# ==============================================================================

tests = [
    # ---- SAMPLE (dari soal) ----
    ("01_sample_n12",       "SAMPLE",       12,    "Sample 1 dari soal: N=12, tukar menguntungkan (f=13)"),
    ("02_sample_n11",       "SAMPLE",       11,    "Sample 2 dari soal: N=11, tidak menukar (f=11)"),

    # ---- MINIMAL ----
    ("03_minimal_n10",      "MINIMAL",      10,    "N minimum (10), tidak menukar lebih baik"),

    # ---- BOUNDARY ----
    ("04_boundary_n1000",   "BOUNDARY",     1000,  "N maksimum (1000), harus rekursi dalam"),
    ("05_boundary_n999",    "BOUNDARY",     999,   "N=999, batas atas minus 1"),

    # ---- EDGE — kasus tidak perlu tukar (f(n)==n) ----
    ("06_edge_no_swap_n23", "EDGE",         23,    "f(23)=23: tidak menukar, keping terakhir sebelum swap menguntungkan"),
    ("07_edge_no_swap_n13", "EDGE",         13,    "f(13)=13: tidak menukar"),

    # ---- EDGE — transisi swap / no-swap ----
    ("08_edge_transition",  "EDGE",         24,    "N=24: multi-level rekursi, f(24)=27 vs wrong=26 (Jebakan 1&5)"),

    # ---- ANTI-WRONG-ANSWER: wrong.py harus salah ----
    # wrong.py: f(n) = max(n, n//2+n//3+n//4) tanpa rekursi
    # Kasus di mana pecahan sendiri perlu dioptimalkan
    ("09_anti_wrong_n48",   "ANTI-WRONG",   48,    "N=48: multi-level depth 2, wrong beri hasil berbeda dari sol"),
    ("10_anti_wrong_n96",   "ANTI-WRONG",   96,    "N=96: multi-level depth 3, wrong jauh berbeda"),
    ("11_anti_wrong_n100",  "ANTI-WRONG",   100,   "N=100: kasus tengah, f=120, wrong=108"),
    ("12_anti_wrong_n36",   "ANTI-WRONG",   36,    "N=36: multi-level, f=41, wrong=39"),

    # ---- RANDOM KECIL ----
    ("13_random_small_1",   "RANDOM-KECIL", random.randint(10, 50),   "Random kecil #1"),
    ("14_random_small_2",   "RANDOM-KECIL", random.randint(10, 50),   "Random kecil #2"),
    ("15_random_small_3",   "RANDOM-KECIL", random.randint(51, 150),  "Random kecil #3 (medium)"),

    # ---- MAX/STRESS ----
    ("16_stress_n998",      "STRESS",       998,   "N=998: mendekati maksimum, stress test"),
    ("17_stress_n997",      "STRESS",       997,   "N=997: mendekati maksimum, stress test"),

    # ---- EDGE — kasus satu level cukup (jebakan 5: hanya 1 level) ----
    ("18_edge_one_level",   "EDGE",         12,    "N=12: satu level tukar cukup, f(6)+f(4)+f(3)=6+4+3=13, mudah dicek manual"),

    # ---- ANTI-OVERFLOW (integer Python tidak overflow, tapi jika C++ pakai int) ----
    # N=1000 → f(1000)=1370, aman di int32. Tidak perlu khusus, tapi dokumentasikan.
    ("19_anti_overflow_n1000", "ANTI-OVERFLOW", 1000, "N=1000: output 1370, aman di int32 (anti-overflow untuk C++)"),

    # ---- EDGE — nilai-nilai di mana wrong hampir benar ----
    ("20_edge_barely_wrong", "ANTI-WRONG",  25,    "N=25: f=27, wrong=26, selisih kecil — mudah lolos test manual"),
]

# Pastikan tidak ada duplikat N dalam kategori yang sama
seen = {}
for prefix, cat, n, desc in tests:
    key = (cat, n)
    if key in seen:
        print(f"WARNING: Duplikat kategori+N: ({cat}, {n}) di {prefix} dan {seen[key]}")
    seen[key] = prefix

# ==============================================================================
# Tulis file .in
# ==============================================================================
print(f"Generating {len(tests)} test cases ke folder '{OUTPUT_DIR}/'")
for prefix, cat, n, desc in tests:
    path = os.path.join(OUTPUT_DIR, f"{prefix}.in")
    with open(path, "w") as fp:
        fp.write(f"{n}\n")
    print(f"  {prefix}.in  N={n}  [{cat}]  {desc}")

print("\nDone. Jalankan:")
print("  python3 validator.py < tests/<file>.in")
print("  python3 sol.py < tests/<file>.in")
