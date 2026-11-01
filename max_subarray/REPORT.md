# Test Report – Maximum Subarray Sum

## Ringkasan Soal

**Masalah:** Diberikan array N bilangan bulat, cari jumlah terbesar dari subarray kontigu (minimal 1 elemen).  
**Constraints:** 1 ≤ N ≤ 100.000, −10⁹ ≤ A[i] ≤ 10⁹, TL 1 detik.  
**Referensi:** Kadane's Algorithm, O(N).

---

## Tabel Test Case

| No  | File                       | Kategori          | N       | Jawaban             | Jebakan yang Diuji                                   | Generator | Status Validator | Status .out      |
|-----|----------------------------|-------------------|---------|---------------------|------------------------------------------------------|-----------|------------------|------------------|
| 01  | `01_sample.in`             | SAMPLE            | 5       | 7                   | Kesesuaian dengan soal                               | hardcoded | ✅ VALID          | brute → VERIFIED |
| 02  | `02_minimal_pos.in`        | MINIMAL           | 1       | 999999999           | N=1 positif mendekati batas atas                     | hardcoded | ✅ VALID          | brute → VERIFIED |
| 03  | `03_minimal_neg.in`        | MINIMAL           | 1       | -1                  | N=1 negatif; max=0 bug: output 0 (salah)             | hardcoded | ✅ VALID          | brute → VERIFIED |
| 04  | `04_boundary.in`           | BOUNDARY          | 4       | 1000000000          | Nilai tepat ±10⁹                                     | hardcoded | ✅ VALID          | brute → VERIFIED |
| 05  | `05_all_negative.in`       | EDGE              | 10      | -26855093           | Semua negatif; max=0 bug: output 0 (salah)           | seeded RNG| ✅ VALID          | brute → VERIFIED |
| 06  | `06_all_zero.in`           | EDGE              | 8       | 0                   | Semua nol; jawaban harus 0 (bukan negatif)           | hardcoded | ✅ VALID          | brute → VERIFIED |
| 07  | `07_all_same_pos.in`       | EDGE              | 6       | 30                  | Semua elemen sama, subarray penuh optimal            | hardcoded | ✅ VALID          | brute → VERIFIED |
| 08  | `08_anti_wrong_all_neg.in` | ANTI-WRONG-ANSWER | 8       | -1                  | Semua negatif; max=0 bug: output 0 (salah)           | hardcoded | ✅ VALID          | brute → VERIFIED |
| 09  | `09_anti_wrong_prefix.in`  | ANTI-WRONG-ANSWER | 5       | -1                  | Seluruh elemen negatif; max=0 bug: output 0 (salah)  | hardcoded | ✅ VALID          | brute → VERIFIED |
| 10  | `10_anti_overflow.in`      | ANTI-OVERFLOW     | 100.000 | 100000000000000     | N=100k semua 10⁹; answer 10¹⁴, perlu 64-bit integer | hardcoded | ✅ VALID          | sol  → VERIFIED  |
| 11  | `11_stress_random.in`      | MAX/STRESS        | 100.000 | 221407050559        | N=100k acak; uji TLE solusi O(N²)                    | seeded RNG| ✅ VALID          | sol  → VERIFIED  |
| 12  | `12_stress_heavy_neg.in`   | MAX/STRESS        | 100.000 | 3094                | N=100k, 90% negatif besar; uji ketahanan             | seeded RNG| ✅ VALID          | sol  → VERIFIED  |
| 13  | `13_small_random_1.in`     | RANDOM-SMALL      | 7       | 270                 | Test acak kecil #1                                   | seeded RNG| ✅ VALID          | brute → VERIFIED |
| 14  | `14_small_random_2.in`     | RANDOM-SMALL      | 15      | 271                 | Test acak kecil #2                                   | seeded RNG| ✅ VALID          | brute → VERIFIED |
| 15  | `15_small_random_3.in`     | RANDOM-SMALL      | 13      | 252                 | Test acak kecil #3                                   | seeded RNG| ✅ VALID          | brute → VERIFIED |

---

## Hasil Validator

```
15 valid / 15 total  →  100% VALID
```

Semua file `.in` melewati pengecekan format dan constraints (validator.py).

---

## Hasil Verifikasi Silang brute.py vs sol.py

```
crosscheck: 200/200 trials matched — brute.py and sol.py agree on all tests.
```

200 test acak kecil (N ∈ [1,50], A[i] ∈ [−10⁶,10⁶], seed=2024): **tidak ada perbedaan**.

---

## Hasil run_tests.py – sol.py (harus lolos semua)

```
Summary: 15 PASS  0 FAIL  0 TLE  (total 15)
```

| Test                       | N       | Waktu   | Status |
|----------------------------|---------|---------|--------|
| 01_sample.in               | 5       | 0.032s  | PASS   |
| 02_minimal_pos.in          | 1       | 0.032s  | PASS   |
| 03_minimal_neg.in          | 1       | 0.030s  | PASS   |
| 04_boundary.in             | 4       | 0.031s  | PASS   |
| 05_all_negative.in         | 10      | 0.034s  | PASS   |
| 06_all_zero.in             | 8       | 0.030s  | PASS   |
| 07_all_same_pos.in         | 6       | 0.033s  | PASS   |
| 08_anti_wrong_all_neg.in   | 8       | 0.036s  | PASS   |
| 09_anti_wrong_prefix.in    | 5       | 0.034s  | PASS   |
| 10_anti_overflow.in        | 100.000 | 0.087s  | PASS   |
| 11_stress_random.in        | 100.000 | 0.106s  | PASS   |
| 12_stress_heavy_neg.in     | 100.000 | 0.096s  | PASS   |
| 13_small_random_1.in       | 7       | 0.034s  | PASS   |
| 14_small_random_2.in       | 15      | 0.039s  | PASS   |
| 15_small_random_3.in       | 13      | 0.042s  | PASS   |

---

## Hasil run_tests.py – wrong.py (harus gagal di test jebakan)

```
Summary: 11 PASS  4 FAIL  0 TLE  (total 15)
```

| Test                       | N       | Waktu   | Status                          |
|----------------------------|---------|---------|---------------------------------|
| 01_sample.in               | 5       | 0.031s  | PASS                            |
| 02_minimal_pos.in          | 1       | 0.037s  | PASS                            |
| **03_minimal_neg.in**      | 1       | 0.046s  | **FAIL** (got=0, want=-1)       |
| 04_boundary.in             | 4       | 0.033s  | PASS                            |
| **05_all_negative.in**     | 10      | 0.045s  | **FAIL** (got=0, want=-26855093)|
| 06_all_zero.in             | 8       | 0.108s  | PASS                            |
| 07_all_same_pos.in         | 6       | 0.053s  | PASS                            |
| **08_anti_wrong_all_neg**  | 8       | 0.043s  | **FAIL** (got=0, want=-1)       |
| **09_anti_wrong_prefix**   | 5       | 0.046s  | **FAIL** (got=0, want=-1)       |
| 10_anti_overflow.in        | 100.000 | 0.119s  | PASS                            |
| 11_stress_random.in        | 100.000 | 0.115s  | PASS                            |
| 12_stress_heavy_neg.in     | 100.000 | 0.114s  | PASS                            |
| 13_small_random_1.in       | 7       | 0.037s  | PASS                            |
| 14_small_random_2.in       | 15      | 0.044s  | PASS                            |
| 15_small_random_3.in       | 13      | 0.043s  | PASS                            |

`wrong.py` **benar-benar gagal di 4 test yang dijebak** (03, 05, 08, 09 — semua array negatif).

---

## Cara Menjalankan

```bash
# Masuk ke folder
cd max_subarray/

# Generate ulang semua test
python3 gen.py

# Validasi semua input
python3 validator.py tests/*.in

# Generate output (kecil=brute, besar=sol)
for f in tests/*.in; do
  N=$(head -1 "$f")
  base="${f%.in}"
  [ "$N" -le 20 ] && python3 brute.py < "$f" > "${base}.out" \
                  || python3 sol.py   < "$f" > "${base}.out"
done

# Verifikasi silang brute vs sol (200 test acak)
python3 crosscheck.py

# Jalankan solusi terhadap semua test
python3 run_tests.py sol.py
python3 run_tests.py wrong.py

# Jalankan satu test manual
python3 sol.py < tests/01_sample.in
```

---

## Daftar Asumsi

1. **"subarray kontigu minimal 1 elemen"** diartikan sebagai: tidak boleh subarray kosong; ketika semua elemen negatif, jawabannya adalah elemen terbesar (paling mendekati nol), bukan 0.
2. **Batas waktu 1 detik** diterapkan secara lunak di `run_tests.py`; proses Python startup menambah ~30ms overhead sehingga solusi O(N) dengan Python3 masih jauh di bawah TL (≈0.1s).
3. **Test "kecil"** didefinisikan sebagai N ≤ 20 untuk pembagian `brute.py` vs `sol.py` dalam pembuatan `.out`.
4. **Verifikasi silang** menggunakan seed 2024 yang terpisah dari seed generator (42) agar trial-trial tersebut independen.
5. **`wrong.py`** didesain hanya untuk menjebak bug `best=0`, bukan TLE — sehingga test overflow (test 10) masih PASS karena jawabannya positif besar.
