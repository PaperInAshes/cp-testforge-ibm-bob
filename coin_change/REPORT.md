# REPORT — Coin Change

## 1. Ringkasan Soal
**Problem:** Coin Change (Unbounded)
**Tipe:** Dynamic Programming (DP) klasik
**Inti:** Diberikan N jenis koin (stok tak terbatas), cari jumlah minimum koin untuk membentuk jumlah X.

## 2. Analisis Format Input/Output
| Komponen | Detail |
|---|---|
| Baris 1 | Dua integer N dan X, dipisah spasi |
| Baris 2 | N integer C[i] berbeda, dipisah spasi |
| Output | Satu integer (minimum koin, atau -1 jika mustahil) |

## 3. Constraints
| Parameter | Batas |
|---|---|
| N | 1 ≤ N ≤ 100 |
| X | 1 ≤ X ≤ 10000 |
| C[i] | 1 ≤ C[i] ≤ 10000 |
| Semua C[i] | Berbeda-beda |
| Stok | Tak terbatas (unbounded) |

## 4. Konsep Inti
- **DP Unbounded:** `dp[j] = min(dp[j], dp[j - c] + 1)` untuk setiap nilai j dari 0 sampai X
- Kompleksitas optimal: O(N × X) = O(100 × 10000) = O(1.000.000) — sangat cukup untuk 1 detik
- Jawaban = `dp[X]` atau -1 jika `dp[X]` masih INF (tidak dapat dibentuk)

## 5. Daftar Jebakan (Traps)

### Jebakan 1: Greedy Gagal
**Deskripsi:** Solusi greedy (selalu ambil koin terbesar yang ≤ sisa) tidak selalu optimal.
**Contoh:** X=6, koin={1,3,4} → greedy: 4+1+1=3 koin, optimal: 3+3=2 koin.
**Efek:** Wrong Answer pada kasus non-canonical coins.
**Ditangkap oleh:** `06_anti_wa_greedy_fail_1`, `07_anti_wa_greedy_fail_2`

### Jebakan 2: Tidak Menangani Kemustahilan (-1)
**Deskripsi:** Lupa mencetak -1 ketika tidak ada kombinasi yang bisa membentuk X.
**Contoh:** X=3, koin={2} → mustahil, harus cetak -1.
**Efek:** Wrong Answer (biasanya output 0 atau nilai besar/INF).
**Ditangkap oleh:** `03_minimal_impossible`, `04_edge_all_coins_gt_x`, `13_edge_impossible_nontrivial`

### Jebakan 3: Inisialisasi DP Salah
**Deskripsi:** Menginisialisasi `dp[0] = 1` (seharusnya 0), atau `dp[i] = 0` untuk i>0 (seharusnya INF).
**Efek:** Wrong Answer — hasil selalu terlalu kecil atau tidak terdeteksi kemustahilan.
**Ditangkap oleh:** `16_anti_wa_dp_init` (X=2, koin=[2], expected=1; dp[0]=1 bug → jawab 2)

### Jebakan 4: Koin Lebih Besar dari X
**Deskripsi:** Tidak menangani kasus di mana semua nilai koin > X.
**Contoh:** X=2, koin={5,7,10} → harus -1.
**Efek:** Wrong Answer atau akses array out-of-bounds.
**Ditangkap oleh:** `04_edge_all_coins_gt_x`

### Jebakan 5: Bounded DP (Koin Dianggap Terbatas / 0-1 Knapsack)
**Deskripsi:** Implementasi 0/1 knapsack alih-alih unbounded — tiap koin hanya boleh dipakai sekali.
**Contoh:** X=4, koin={2} → bounded: mustahil, unbounded: 2 koin.
**Efek:** Wrong Answer pada kasus yang perlu memakai koin yang sama lebih dari sekali.
**Ditangkap oleh:** `08_anti_wa_unbounded`

### Jebakan 6: Koin dengan Nilai = X (Tepat Satu Koin)
**Deskripsi:** Lupa mempertimbangkan bahwa satu koin mungkin tepat sama dengan X.
**Contoh:** X=5, koin={3,5,8} → jawaban 1.
**Efek:** Wrong Answer (jawaban salah atau tidak terdeteksi).
**Ditangkap oleh:** `05_edge_coin_equals_x`

### Jebakan 7: TLE dari Solusi Rekursif Tanpa Memoization
**Deskripsi:** Rekursi naif tanpa DP/memo pada X=10000 → kompleksitas eksponensial.
**Efek:** Time Limit Exceeded pada input maksimum.
**Ditangkap oleh:** `09_boundary_max_x_coin1`, `10_max_stress`

### Jebakan 8: Overflow Integer (C/C++ 32-bit)
**Deskripsi:** Menggunakan `int` untuk nilai INF = 99999999, saat ditambah 1 bisa overflow negatif.
**Contoh:** `if (dp[j-c] + 1 < dp[j])` — jika dp[j-c] = INT_MAX, overflow.
**Efek:** Wrong Answer di C++ (Python tidak masalah karena integer arbitrary-precision).
**Ditangkap oleh:** `12_anti_overflow`

## 6. Asumsi Eksplisit
1. Input selalu memiliki tepat 2 baris (validator mengecek ini).
2. Tidak ada constraint eksplisit urutan koin — implementasi tidak bergantung urutan.
3. "Nilai C berbeda-beda" = tidak ada dua koin dengan nilai yang sama. Validator mengecek.
4. Karena soal ini memiliki jawaban tunggal (jumlah minimum adalah unik), checker sederhana (perbandingan teks integer) sudah cukup. Checker khusus tetap disediakan sebagai `checker.py`.
5. Batas waktu diterapkan per test. Python 3 digunakan sebagai runtime untuk semua .py.

## 7. Tabel Test

| No | File | Kategori | Ukuran | Jebakan yang Diuji | Status |
|---|---|---|---|---|---|
| 01 | `01_sample.in` | SAMPLE | N=3, X=11 | Baseline | ✅ VERIFIED (brute) |
| 02 | `02_minimal_possible.in` | MINIMAL | N=1, X=1 | N minimum, X minimum | ✅ VERIFIED (brute) |
| 03 | `03_minimal_impossible.in` | MINIMAL | N=1, X=3 | Jebakan 2 (-1) | ✅ VERIFIED (brute) |
| 04 | `04_edge_all_coins_gt_x.in` | EDGE | N=3, X=2 | Jebakan 2+4 | ✅ VERIFIED (brute) |
| 05 | `05_edge_coin_equals_x.in` | EDGE | N=3, X=5 | Jebakan 6 (coin=X) | ✅ VERIFIED (brute) |
| 06 | `06_anti_wa_greedy_fail_1.in` | ANTI-WA | N=3, X=6 | Jebakan 1 (greedy) | ✅ VERIFIED (brute) |
| 07 | `07_anti_wa_greedy_fail_2.in` | ANTI-WA | N=4, X=30 | Jebakan 1 (greedy kuat) | ✅ VERIFIED (brute) |
| 08 | `08_anti_wa_unbounded.in` | ANTI-WA | N=1, X=4 | Jebakan 5 (bounded) | ✅ VERIFIED (brute) |
| 09 | `09_boundary_max_x_coin1.in` | MAX/STRESS | N=1, X=10000 | Jebakan 7 (TLE) | ✅ VERIFIED (sol) |
| 10 | `10_max_stress.in` | MAX/STRESS | N=100, X=10000 | Jebakan 7+8 | ✅ VERIFIED (sol) |
| 11 | `11_boundary_x1.in` | BOUNDARY | N=3, X=1 | X minimum dengan pilihan | ✅ VERIFIED (brute) |
| 12 | `12_anti_overflow.in` | ANTI-OVERFLOW | N=2, X=10000 | Jebakan 8 (overflow) | ✅ VERIFIED (sol) |
| 13 | `13_edge_impossible_nontrivial.in` | EDGE | N=2, X=7 | Jebakan 2 (mustahil non-trivial) | ✅ VERIFIED (brute) |
| 14 | `14_random_small_1.in` | RANDOM-SMALL | N=5, X=7 | Variasi acak | ✅ VERIFIED (brute) |
| 15 | `15_random_small_2.in` | RANDOM-SMALL | N=7, X=55 | Variasi acak | ✅ VERIFIED (brute) |
| 16 | `16_anti_wa_dp_init.in` | ANTI-WA | N=1, X=2 | Jebakan 3 (dp init) | ✅ VERIFIED (brute) |

## 8. Hasil Verifikasi

### Validator
```
Semua 16 file .in: OK (validator.py)
```

### Cross-verify brute.py vs sol.py (200 random kecil)
```
200/200 PASS — brute == sol untuk semua 200 test acak kecil ✓
```

### run_tests sol.py
```
SUMMARY: PASS=16  WA=0  TLE=0  RE=0  ← LOLOS SEMUA ✓
```

### run_tests wrong.py (harus gagal ≥1)
```
SUMMARY: PASS=9  WA=7  TLE=0  RE=0
WA pada: 03_minimal_impossible, 04_edge_all_coins_gt_x, 06_anti_wa_greedy_fail_1,
         07_anti_wa_greedy_fail_2, 10_max_stress, 13_edge_impossible_nontrivial,
         15_random_small_2  ← GAGAL SEBANYAK 7 ✓
```

### run_tests slow.py (harus TLE ≥1)
```
SUMMARY: PASS=15  WA=0  TLE=1  RE=0
TLE pada: 10_max_stress (3005.3ms > 1.0s)  ← TLE ✓
```

## 9. Cara Memakai untuk Solusi Sendiri

```bash
# Masuk ke folder
cd coin_change

# Test solusi Python kamu (semua test)
python3 run_tests.py my_solution.py

# Test solusi C++ (dikompilasi otomatis dengan g++)
python3 run_tests.py my_solution.cpp

# Jalankan satu test manual
python3 my_solution.py < tests/01_sample.in

# Bandingkan output kamu dengan expected (diff)
python3 my_solution.py < tests/06_anti_wa_greedy_fail_1.in | diff - tests/06_anti_wa_greedy_fail_1.out

# Validasi input kustom kamu
python3 validator.py my_test.in

# Gunakan checker (input.in expected.out actual.out)
python3 checker.py tests/06_anti_wa_greedy_fail_1.in \
        tests/06_anti_wa_greedy_fail_1.out \
        <(python3 my_solution.py < tests/06_anti_wa_greedy_fail_1.in)

# Cross-verify ulang brute vs sol
python3 cross_verify.py

# Generate ulang semua test (seed tetap = reproducible)
python3 gen.py
```

### Daftar File
| File | Peran |
|---|---|
| `problem.md` | Soal lengkap |
| `sol.py` | Solusi efisien (DP O(N×X)) — referensi utama |
| `brute.py` | Solusi benar lambat (BFS) — untuk verifikasi |
| `wrong.py` | Solusi salah (greedy) — untuk memastikan test WA |
| `slow.py` | Solusi benar tapi TLE (rekursi tanpa memo) |
| `validator.py` | Cek format & constraints input |
| `checker.py` | Cek kebenaran output (integer comparison) |
| `gen.py` | Generator test (seed=42, reproducible) |
| `run_tests.py` | Runner otomatis (.py dan .cpp) |
| `cross_verify.py` | Verifikasi silang brute vs sol (200 test) |
| `tests/*.in` | 16 file input |
| `tests/*.out` | 16 file expected output (dari eksekusi kode) |
