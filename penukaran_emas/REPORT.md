# REPORT — Penukaran Emas

## Ringkasan Soal

**Deskripsi:** Diberikan N gram emas, boleh menukar 1 keping N gram menjadi tiga keping N//2, N//3, N//4 gram. Proses dapat dilakukan berulang. Cari total berat maksimum.

**Rumus inti:**
```
f(n) = max(n, f(n//2) + f(n//3) + f(n//4))
```

**Input:** 10 ≤ N ≤ 1.000  
**Output:** Satu bilangan bulat

---

## Analisis Format Input/Output

- Input: satu baris, satu integer N
- Output: satu baris, satu integer
- Tidak ada whitespace tambahan yang diperlukan

## Constraints

| Parameter | Nilai |
|-----------|-------|
| N minimum | 10    |
| N maksimum | 1.000 |
| Pembagian | floor (integer division) |
| Time limit | 1 detik |
| Memory limit | 16 MB |

## Konsep Inti

Rekursi dengan memoization (top-down DP). Subproblem: f(n) untuk semua n yang muncul dalam rekursi tree dari N=1000. Karena N ≤ 1000, jumlah subproblem unik sangat terbatas (O(N)), sehingga memoization membuat kompleksitas O(N).

---

## Daftar Jebakan

| No | Jebakan | Deskripsi | Contoh Kegagalan |
|----|---------|-----------|-----------------|
| J1 | Tidak rekursi pada pecahan | f(n) = max(n, n//2+n//3+n//4) tanpa merekursi pada pecahan | N=24: wrong=26, sol=27 |
| J2 | Rekursi tanpa memoization | Subproblem dihitung berulang, kompleksitas membengkak | TLE pada N besar dengan work tambahan |
| J3 | Pembulatan salah (round/ceil bukan floor) | Menggunakan round() alih-alih // | Hasil beda pada nilai N tertentu |
| J4 | Base case hilang (N=0 atau N<0) | Stack overflow atau hasil salah untuk pecahan kecil | f(4//4)=f(1): f(1//2)=f(0) perlu return 0 |
| J5 | Hanya satu level penukaran | Sama dengan J1 — anggap setiap keping hanya boleh ditukar sekali | N=24, N=48, N=100 |
| J6 | Off-by-one batas atas | Tidak menguji N=1000, hanya sampai N=999 | N=1000 bisa menghasilkan jawaban berbeda |

---

## Tabel Test

| No  | File                          | Kategori       | N    | Jebakan yang Diuji          | .out  | Status Validator |
|-----|-------------------------------|----------------|------|----------------------------|-------|-----------------|
| 01  | 01_sample_n12.in              | SAMPLE         | 12   | Sample soal, tukar 1 level | 13    | ✓ OK |
| 02  | 02_sample_n11.in              | SAMPLE         | 11   | Sample soal, tidak tukar   | 11    | ✓ OK |
| 03  | 03_minimal_n10.in             | MINIMAL        | 10   | N minimum, tidak tukar     | 10    | ✓ OK |
| 04  | 04_boundary_n1000.in          | BOUNDARY       | 1000 | J6: batas atas, rekursi dalam | 1370 | ✓ OK |
| 05  | 05_boundary_n999.in           | BOUNDARY       | 999  | J6: N=999, mendekati maks  | 1370  | ✓ OK |
| 06  | 06_edge_no_swap_n23.in        | EDGE           | 23   | J4/J5: tidak menukar optimal | 23  | ✓ OK |
| 07  | 07_edge_no_swap_n13.in        | EDGE           | 13   | J4/J5: tidak menukar optimal | 13  | ✓ OK |
| 08  | 08_edge_transition.in         | EDGE           | 24   | J1/J5: multi-level, wrong=26 vs sol=27 | 27 | ✓ OK |
| 09  | 09_anti_wrong_n48.in          | ANTI-WRONG     | 48   | J1/J5: multi-level depth 2 | 57    | ✓ OK |
| 10  | 10_anti_wrong_n96.in          | ANTI-WRONG     | 96   | J1/J5: multi-level depth 3 | 119   | ✓ OK |
| 11  | 11_anti_wrong_n100.in         | ANTI-WRONG     | 100  | J1/J5: tengah, f=120 vs wrong=108 | 120 | ✓ OK |
| 12  | 12_anti_wrong_n36.in          | ANTI-WRONG     | 36   | J1/J5: f=41 vs wrong=39   | 41    | ✓ OK |
| 13  | 13_random_small_1.in          | RANDOM-KECIL   | 50   | Random, verifikasi umum    | 57    | ✓ OK |
| 14  | 14_random_small_2.in          | RANDOM-KECIL   | 17   | Random kecil, tidak tukar  | 17    | ✓ OK |
| 15  | 15_random_small_3.in          | RANDOM-KECIL   | 54   | Random medium              | 60    | ✓ OK |
| 16  | 16_stress_n998.in             | STRESS         | 998  | J2/J6: stress mendekati max | 1370 | ✓ OK |
| 17  | 17_stress_n997.in             | STRESS         | 997  | J2/J6: stress mendekati max | 1370 | ✓ OK |
| 18  | 18_edge_one_level.in          | EDGE           | 12   | Verifikasi satu level cukup (beda tujuan dari test 01) | 13 | ✓ OK |
| 19  | 19_anti_overflow_n1000.in     | ANTI-OVERFLOW  | 1000 | J3: output 1370 aman int32 | 1370  | ✓ OK |
| 20  | 20_edge_barely_wrong.in       | ANTI-WRONG     | 25   | J1: selisih kecil wrong=26 vs sol=27 | 27 | ✓ OK |

---

## Hasil Verifikasi

### Validator (20/20 OK)
Semua 20 file `.in` lulus validator dengan exit code 0.

### Verifikasi Silang brute.py vs sol.py
```
200 kasus acak N ∈ [10, 200], seed=1337
→ ALL 200 CASES MATCH (brute == sol)
```

### Sumber .out
| Solver | Digunakan untuk |
|--------|----------------|
| brute.py | N ≤ 500 (test 01–13, 14–15, 18, 20) |
| sol.py   | N > 500 (test 04, 05, 16, 17, 19) |

---

## Hasil run_tests

### sol.py — harus PASS semua ✅
```
PASS=20  WA=0  TLE=0  RE=0
✓ SEMUA 20 TEST LULUS
```

### wrong.py — harus gagal minimal 1 ✅
```
PASS=7  WA=13  TLE=0  RE=0
✗ 13/20 TEST GAGAL (WA)
```
WA pada: N=1000,999,24,48,96,100,36,50,54,998,997,1000(ulang),25

### slow.py — harus TLE minimal 1 ✅
```
PASS=15  WA=0  TLE=5  RE=0
✗ 5/20 TEST GAGAL (TLE)
```
TLE pada: N=1000,999,998,997,1000(ulang) → ~1.8–2.0s (>1.0s limit)

---

## Self-Check

| Kriteria | Status |
|----------|--------|
| Semua jebakan tertangkap oleh minimal 1 test | ✅ |
| Tidak ada dua test kembar (tujuan unik) | ✅ |
| wrong.py gagal minimal 1 test | ✅ (gagal 13) |
| slow.py TLE minimal 1 test | ✅ (TLE 5) |
| Semua .out dari eksekusi kode | ✅ |
| Semua .in lulus validator | ✅ (20/20) |
| brute == sol (200 kasus acak) | ✅ |

---

## Asumsi Eksplisit

1. **N selalu dalam range [10, 1000]** — sesuai constraints soal, validator menolak di luar range
2. **Proses penukaran tidak terbatas** — dapat dilakukan berulang sampai tidak menguntungkan
3. **"Tidak menukar" selalu valid** — Pak Dengklek boleh mempertahankan keping aslinya
4. **Integer arithmetic** — semua operasi pembagian menggunakan floor division (Python `//`)
5. **slow.py menggunakan dummy loop** — karena rekursi murni pada N≤1000 masih terlalu cepat untuk TLE natural, ditambahkan komputasi dummy untuk mensimulasikan TLE. Dalam kompetisi nyata, "lambat" berasal dari algoritma yang salah (misalnya tidak memakai DP)

---

## Cara Memakai untuk Solusi Sendiri

```bash
# Masuk ke folder
cd penukaran_emas

# Uji solusi Python Anda
python3 run_tests.py my_sol.py

# Uji solusi C++
python3 run_tests.py my_sol.cpp
# (g++ harus tersedia; dikompilasi otomatis)

# Validasi satu file input secara manual
python3 validator.py < tests/01_sample_n12.in

# Lihat isi test tertentu
cat tests/08_edge_transition.in   # input
cat tests/08_edge_transition.out  # output yang benar

# Generate ulang test (seed tetap, hasil sama)
python3 gen.py

# Verifikasi silang manual
python3 -c "
import subprocess
for n in [24, 100, 1000]:
    r = subprocess.run(['python3','sol.py'], input=str(n), capture_output=True, text=True)
    print(f'N={n} -> {r.stdout.strip()}')
"

# Cek apakah solusi Anda berbeda dari sol.py
python3 -c "
import subprocess, glob
for f in sorted(glob.glob('tests/*.in')):
    inp = open(f).read()
    expected = open(f.replace('.in','.out')).read().strip()
    got = subprocess.run(['python3','MY_SOL.py'], input=inp, capture_output=True, text=True).stdout.strip()
    if got != expected:
        print(f'MISMATCH {f}: expected={expected}, got={got}')
"
```
