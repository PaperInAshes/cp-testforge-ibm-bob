# REPORT — Longest Increasing Subsequence

## Analisis Soal

### Format Input/Output
- **Input:** Baris 1 = N; Baris 2 = N bilangan bulat dipisah spasi
- **Output:** Satu bilangan bulat (panjang LIS yang strictly increasing)

### Constraints
| Parameter | Nilai |
|-----------|-------|
| N | 1 ≤ N ≤ 100,000 |
| A[i] | −10^9 ≤ A[i] ≤ 10^9 |
| Time limit | 1 detik |

### Konsep Inti
- **LIS (Longest Increasing Subsequence) STRICTLY increasing**: panjang terpanjang subsequence (tidak harus kontigu) dimana `A[i] < A[j]` untuk setiap elemen berurutan.
- Solusi optimal: **O(N log N)** menggunakan patience sorting / binary search dengan array `tails`.
  - `tails[i]` = nilai terkecil dari semua elemen penutup LIS panjang `i+1`.
  - Untuk setiap elemen baru, gunakan `bisect_left` (bukan `bisect_right`) karena strictly increasing.
- Solusi naif: **O(N²) DP** — benar tapi TLE untuk N = 100,000.

### Asumsi Eksplisit
1. "Strictly increasing" artinya `A[i] < A[j]` (bukan ≤). Soal menyebutkan ini secara eksplisit.
2. Baris ke-2 selalu ada meskipun N=1 (berisi tepat satu bilangan).
3. Spasi separator tunggal diterima; spasi berlebih di akhir baris diabaikan.
4. A[i] bisa negatif (constraints: ≥ −10^9).

---

## Daftar Jebakan (Trap List)

| # | Jebakan | Dampak | Test yang Menangkap |
|---|---------|--------|---------------------|
| T1 | Menggunakan **`bisect_right`** bukan `bisect_left` → mengizinkan elemen sama masuk subsequence (non-strictly increasing) | WA | test_07, test_10, test_13, test_19 |
| T2 | Solusi **O(N²) DP** — benar tapi TLE pada N=100,000 | TLE | test_12, test_13, test_14, test_20 |
| T3 | **Lupa kasus N=1** — return 0 atau crash | WA/RE | test_02 |
| T4 | Menukar `bisect_left` ↔ `bisect_right` (keliru arah) sehingga duplikat masuk `tails` | WA | test_07, test_10, test_19 |
| T5 | Tidak menangani **nilai negatif** dengan benar (misal: mencoba abs value) | WA | test_09, test_15 |
| T6 | Mengira LIS = panjang sorted-distinct array, bukan subsequence optimal | WA | test_06, test_08, test_18 |
| T7 | **Integer overflow** di C++ saat diff dua A[i] (bisa 2×10^9 > INT_MAX) | WA di C++ | test_11 |
| T8 | Off-by-one atau early-return sebelum semua elemen diproses | WA | test_05, test_08 |

---

## Tabel Test

| No | File | Kategori | N | Jebakan Diuji | Jawaban | Sumber .out |
|----|------|----------|---|---------------|---------|-------------|
| 01 | test_01_sample | SAMPLE | 6 | — | 3 | brute |
| 02 | test_02_minimal_n1 | MINIMAL | 1 | T3 (N=1) | 1 | brute |
| 03 | test_03_minimal_n2_inc | MINIMAL | 2 | — | 2 | brute |
| 04 | test_04_minimal_n2_dec | MINIMAL | 2 | T6 | 1 | brute |
| 05 | test_05_edge_single_increase | EDGE | 1000 | T8 (off-by-one) | 1000 | brute |
| 06 | test_06_edge_decreasing | EDGE | 500 | T6 (sorted≠LIS) | 1 | brute |
| 07 | test_07_edge_all_equal | EDGE | 1000 | T1/T4 (bisect_right) | 1 | brute |
| 08 | test_08_edge_almost_sorted | EDGE | 998 | T6, T8 | 998 | brute |
| 09 | test_09_anti_wa_negative | ANTI-WA | 6 | T5 (negatif) | 6 | brute |
| 10 | test_10_anti_wa_non_strict | ANTI-WA | 5 | T1/T4 (non-strict) | 3 | brute |
| 11 | test_11_anti_overflow | ANTI-OVERFLOW | 6 | T7 (±1e9 diff) | 4 | brute |
| 12 | test_12_stress_max_sorted | MAX/STRESS | 100000 | T2 (TLE O(N²)) | 100000 | sol |
| 13 | test_13_stress_max_equal | MAX/STRESS | 100000 | T1+T2 (TLE+WA) | 1 | sol |
| 14 | test_14_stress_max_random | MAX/STRESS | 100000 | T2 (TLE O(N²)) | 625 | sol |
| 15 | test_15_boundary_neg_inc | BOUNDARY | 200 | T5 (negatif boundary) | 200 | brute |
| 16 | test_16_random_small_1 | RANDOM-SMALL | 20 | general | 7 | brute |
| 17 | test_17_random_small_2 | RANDOM-SMALL | 30 | general | 9 | brute |
| 18 | test_18_edge_zigzag | EDGE | 100 | T6, T8 (zigzag) | 51 | brute |
| 19 | test_19_anti_wa_dup_then_larger | ANTI-WA | 11 | T1/T4 (duplikat+1) | 2 | brute |
| 20 | test_20_stress_max_reverse | MAX/STRESS | 100000 | T2 (TLE, reverse) | 1 | sol |

---

## Hasil Validator

Semua **20/20** file `.in` lulus validator (`python3 validator.py`):
```
OK: tests/test_01_sample.in
OK: tests/test_02_minimal_n1.in
...
OK: tests/test_20_stress_max_reverse.in
```
Tidak ada file yang gagal validasi.

---

## Hasil Verifikasi Silang brute vs sol

- **Test kecil (N ≤ 1000) di folder tests/**: semua 16 test → brute == sol ✓
- **200 random kecil tambahan** (`cross_verify.py`, seed=1234, N≤50, A[i]∈[-100,100]): semua 200 → brute == sol ✓

---

## Hasil run_tests

### sol.py (solusi efisien O(N log N))
```
Results: 20 tests — 20 PASS, 0 WA, 0 TLE, 0 RE  ✓
```

### wrong.py (bug: bisect_right → non-strictly increasing)
```
Results: 20 tests — 16 PASS, 4 WA, 0 TLE, 0 RE
WA on: test_07_edge_all_equal, test_10_anti_wa_non_strict,
       test_13_stress_max_equal, test_19_anti_wa_dup_then_larger  ✓
```

### slow.py (benar tapi O(N²))
```
Results: 20 tests — 16 PASS, 0 WA, 4 TLE, 0 RE
TLE on: test_12_stress_max_sorted, test_13_stress_max_equal,
        test_14_stress_max_random, test_20_stress_max_reverse  ✓
```

Semua syarat terpenuhi:
- ✅ sol.py lolos **semua** test
- ✅ wrong.py gagal **minimal 1** test (gagal 4)
- ✅ slow.py TLE **minimal 1** test (TLE 4)

---

## Checker

Tidak diperlukan. Output LIS adalah satu bilangan bulat yang **unik** — tidak ada ambiguitas dalam jawaban yang benar.

---

## Cara Memakai untuk Solusi Sendiri

```bash
# Masuk ke folder
cd longest_increasing_subsequence

# Uji solusi Python
python3 run_tests.py my_solution.py

# Uji solusi C++ (dikompilasi otomatis dengan g++ -O2)
python3 run_tests.py my_solution.cpp

# Uji satu test manual
python3 my_solution.py < tests/test_01_sample.in

# Validasi satu file input
python3 validator.py tests/test_01_sample.in

# Validasi semua input
for f in tests/*.in; do python3 validator.py "$f"; done

# Verifikasi silang brute vs sol (200 random kecil)
python3 cross_verify.py

# Generate ulang semua test (seed tetap = 42)
python3 gen.py
```

**Interpretasi hasil run_tests.py:**
| Status | Arti |
|--------|------|
| `PASS` | Output tepat sama dengan .out |
| `WA`   | Output berbeda dari .out |
| `TLE`  | Melebihi batas waktu efektif (1.5× untuk Python, 1× untuk C++) |
| `RE`   | Runtime error (crash, exception, exit code ≠ 0) |

> **Catatan TLE Python:** `run_tests.py` menggunakan batas 1.5 detik untuk `.py` (toleransi overhead interpreter). Pada sistem judge C++ yang sesungguhnya, batas tetap 1 detik.
