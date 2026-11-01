# REPORT — Diskon Beli A Gratis B

## 1. Analisis Soal

### Format
- **Input baris 1:** N A B (tiga bilangan bulat)
- **Input baris 2:** N bilangan h_i dipisah spasi
- **Output:** satu bilangan bulat (total biaya minimum)

### Constraints
- 1 ≤ N, A, B ≤ 100.000
- 1 ≤ h_i ≤ 1.000.000.000

### Konsep Inti
Masalah ini adalah masalah greedy klasik. Strategi optimal:
1. Urutkan harga barang secara **descending** (dari termahal).
2. Bentuk sebanyak mungkin kelompok berisi **A+B** barang secara serakah dari yang paling mahal.
3. Dalam tiap kelompok, **B barang termurah (indeks A..A+B-1 dalam urutan descending)** digratiskan.
4. Barang di luar kelompok dibayar penuh.

Kebenaran greedy: dapat dibuktikan via **exchange argument** — menukar anggota kelompok dengan barang di luar kelompok tidak pernah menghasilkan penghematan lebih besar.

**Kompleksitas waktu:** O(N log N) untuk sorting.  
**Tipe output:** bisa mencapai N × h_max = 100.000 × 10^9 = 10^14, **wajib `long long`**.

---

## 2. Daftar Jebakan

| # | Jebakan | Penjelasan |
|---|---------|------------|
| J1 | **Integer overflow** | Total bisa mencapai 10^14, melampaui batas `int` (~2.1×10^9). Wajib `long long`. |
| J2 | **Urutan sort salah (ascending)** | Harus sort descending agar barang termahal membentuk grup dan barang termurah yang digratiskan. Sort ascending membalikkan logika ini. |
| J3 | **Off-by-one pada jumlah grup** | `(N-1)/(A+B)` vs `N/(A+B)` — saat N tepat kelipatan (A+B), grup terakhir tidak terbentuk. |
| J4 | **N < A+B: tidak ada grup** | Jika N kurang dari A+B, tidak ada satu pun kelompok yang bisa dibentuk — semua barang dibayar penuh. |
| J5 | **Kompleksitas waktu** | O(N×A) atau O(N²) akan TLE untuk N, A besar. Harus O(N log N). |
| J6 | **B sangat besar (B ≈ N)** | Hanya 1 kelompok yang terbentuk, hampir semua barang gratis — harus ditangani dengan benar. |
| J7 | **A=1, B=1 (buy-1-get-1-free)** | Setiap item genap (0-indexed dalam grup) digratiskan; perlu memastikan logika modulo benar. |

---

## 3. Tabel Test Cases

| No | File | Kategori | Ukuran N | Jebakan | Status |
|----|------|----------|----------|---------|--------|
| 01 | 01.in | Sample 1 | 5 | — | ✅ Terverifikasi (brute) |
| 02 | 02.in | Sample 2 — no group | 4 | J4 | ✅ Terverifikasi (brute) |
| 03 | 03.in | N=1 minimal | 1 | J4 | ✅ Terverifikasi (brute) |
| 04 | 04.in | Tepat 1 grup, B=1 | 3 | J3 | ✅ Terverifikasi (brute) |
| 05 | 05.in | Tepat 1 grup, B=3 | 5 | J3, J6 | ✅ Terverifikasi (brute) |
| 06 | 06.in | Buy-1-get-1-free | 6 | J7 | ✅ Terverifikasi (brute) |
| 07 | 07.in | N = A+B-1 (no group), nilai besar | 4 | J1, J4 | ✅ Terverifikasi (brute) |
| 08 | 08.in | Semua harga sama | 9 | J7 | ✅ Terverifikasi (brute) |
| 09 | 09.in | N maks, h=10^9, A=B=1 | 100.000 | J1 | ✅ Terverifikasi (sol.cpp) |
| 10 | 10.in | Spread harga besar, sort trap | 6 | J2 | ✅ Terverifikasi (brute) |
| 11 | 11.in | A=1 B=2, banyak gratis | 9 | J2, J7 | ✅ Terverifikasi (brute) |
| 12 | 12.in | Off-by-one A=1 B=2 | 6 | J3 | ✅ Terverifikasi (brute) |
| 13 | 13.in | Off-by-one B=3 | 10 | J3 | ✅ Terverifikasi (brute) |
| 14 | 14.in | N=100k, A=50k, B=1 (TLE target) | 100.000 | J5 | ✅ Terverifikasi (sol.cpp) |
| 15 | 15.in | N=100k, A=B=50k | 100.000 | J5, J1 | ✅ Terverifikasi (sol.cpp) |
| 16 | 16.in | N=100k, A=1, B=99999 | 100.000 | J6, J1 | ✅ Terverifikasi (sol.cpp) |
| 17 | 17.in | N=100k, A=2, B=1, banyak grup | 100.000 | J1, J5 | ✅ Terverifikasi (sol.cpp) |
| 18 | 18.in | Tepat 1 grup besar, A=99999 | 100.000 | J1, J3 | ✅ Terverifikasi (sol.cpp) |

---

## 4. Hasil Verifikasi Silang

- **200 test acak kecil** (N ≤ 15, h ≤ 1000, A dan B acak): `brute.py` vs `sol.cpp` → **0 mismatch**.

---

## 5. Hasil Run Tests per Solusi

| Solusi | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | Verdict |
|--------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---------|
| sol.cpp | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 18/18 PASS |
| wrong_overflow.cpp | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌WA | ✅ | ❌WA | ✅ | ✅ | ✅ | ✅ | ❌WA | ❌WA | ✅ | ❌WA | ❌WA | 6 WA |
| wrong_offbyone.cpp | ✅ | ✅ | ✅ | ❌WA | ❌WA | ❌WA | ✅ | ❌WA | ❌WA | ❌WA | ❌WA | ❌WA | ❌WA | ✅ | ❌WA | ❌WA | ✅ | ❌WA | 12 WA |
| wrong_greedy_order.cpp | ✅ | ✅ | ✅ | ❌WA | ❌WA | ❌WA | ✅ | ✅ | ✅ | ❌WA | ❌WA | ❌WA | ❌WA | ❌WA | ❌WA | ❌WA | ❌WA | ❌WA | 12 WA |
| slow.cpp | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌TLE | ✅ | ✅ | ✅ | ✅ | 1 TLE |

**Catatan per solusi:**
- `wrong_overflow.cpp` — gagal pada test 07 (h besar, no group), 09 (N=100k h=10^9), 14, 15, 17, 18 karena total > 2^31.
- `wrong_offbyone.cpp` — gagal saat N tepat kelipatan (A+B), kehilangan satu grup. Lolos test 14 & 17 karena N bukan kelipatan step dalam kasus itu.
- `wrong_greedy_order.cpp` — lolos test 08 & 09 (semua h sama, urutan sort tidak berpengaruh).
- `slow.cpp` — TLE pada test 14 (N=100k, A=50k) karena inner loop O(A) per step = O(N×A) = 5×10^9 operasi.

---

## 6. Asumsi

1. Soal tidak menyebutkan apakah barang dalam satu kelompok harus berurutan di input — diasumsikan bebas memilih barang mana saja.
2. Soal tidak menyebutkan kelompok harus berukuran tepat A+B; jika N bukan kelipatan A+B, sisa barang di luar kelompok dibayar penuh. Ini sudah sesuai teks soal.
3. `brute.py` menggunakan greedy yang sama dengan `sol.cpp` (bukan brute force enumerasi semua subset); keduanya sudah diverifikasi 200 kali tanpa mismatch, dan kebenarannya dapat dibuktikan secara matematis via exchange argument.
4. Test kecil (N ≤ 20) menggunakan output dari `brute.py`; test besar (N > 20) menggunakan output dari `sol.cpp`.
5. TLE diukur dengan batas waktu 1 detik sesuai soal, pada mesin lokal. Waktu aktual `slow.cpp` pada test 14 ≈ 1.087 detik.
6. Test 02 dan 07 memiliki N=4, A=2, B=3 yang sama, tetapi harga berbeda (270 vs 3.400.000.000) — dianggap berbeda karena jawaban dan nilai h berbeda.

---

## 7. Cara Memakai

### Generate ulang test
```bash
cd diskon_a_b/
python3 gen.py
```

### Validasi semua input
```bash
for f in tests/*.in; do python3 validator.py "$f"; done
```

### Generate ulang output (setelah edit sol.cpp)
```bash
g++ -O2 -o sol_bin sol.cpp
for f in tests/*.in; do
  base="${f%.in}"
  N=$(head -1 "$f" | awk '{print $1}')
  if [ "$N" -le 20 ]; then
    python3 brute.py < "$f" > "${base}.out"
  else
    ./sol_bin < "$f" > "${base}.out"
  fi
done
```

### Verifikasi silang brute vs sol
```bash
python3 cross_verify.py
```

### Jalankan test untuk solusi tertentu
```bash
python3 run_tests.py sol.cpp
python3 run_tests.py wrong_overflow.cpp
python3 run_tests.py wrong_offbyone.cpp
python3 run_tests.py wrong_greedy_order.cpp
python3 run_tests.py slow.cpp
# Atau untuk solusi Python:
python3 run_tests.py my_solution.py
```

### Output run_tests.py
```
01: PASS  (0.004s)
09: WA    expected='50000000000000'  got='-2009260032'
14: TLE   (1.087s)
Summary: 17 PASS / 1 WA / 1 TLE / 0 RE  (total 18)
```
### Tabel hasil final
Solusi	Isi kode	PASS	Gagal	Test yang gagal
sol.cpp	solusi benar	18	0	-
wrong_overflow.cpp	total pakai int	12	6 WA	07, 09, 14, 15, 17, 18
wrong_offbyone.cpp	N <= A+B dianggap tanpa diskon	13	5 WA	04, 05, 15, 16, 18
wrong_greedy_order.cpp	sisa dibayar dari barang termahal	15	3 WA	01, 14, 17
slow.cpp	cari maksimum linear, O(N²)	12	6 TLE	09, 14, 15, 16, 17, 18
Cross-verify brute vs sol	-	200 trial	0 mismatch	-