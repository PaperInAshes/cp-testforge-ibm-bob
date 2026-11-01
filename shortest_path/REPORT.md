# REPORT — Shortest Path Test Suite

## 1. Ringkasan Soal

| Atribut | Detail |
|---|---|
| Judul | Shortest Path |
| Tipe Graf | Tak berarah, berbobot positif |
| Simpul | 1 → N |
| Constraints | 2 ≤ N ≤ 100.000, 1 ≤ M ≤ 200.000, 1 ≤ w ≤ 10⁹ |
| Batas Waktu | 2 detik |
| Self-loop/Multi-edge | Diperbolehkan |

## 2. Analisis Format Input/Output

**Input:**
- Baris 1: `N M` (jumlah simpul, jumlah sisi)
- M baris berikutnya: `u v w` (sisi tak berarah antara u dan v dengan bobot w)

**Output:**
- Satu bilangan bulat: jarak terpendek dari simpul 1 ke simpul N
- Cetak `-1` jika tidak ada jalur

**Konsep Inti:**
- Algoritma Dijkstra dengan min-heap (priority queue) untuk graf berbobot non-negatif
- Kompleksitas optimal: O((N + M) log N)
- Diperlukan tipe data 64-bit (Python int otomatis, C++ gunakan `long long`)

## 3. Daftar Jebakan (Minimal 4)

| ID | Jebakan | Deskripsi | Test Penangkap |
|---|---|---|---|
| T1 | **BFS Tanpa Bobot** | Menggunakan BFS biasa yang tidak mempertimbangkan bobot sisi. BFS mencari "jalur dengan hop terkecil", bukan jalur terpendek berbobot. Akan salah jika ada jalur panjang tapi ringan vs jalur pendek tapi berat. | 04, 05, 11, 16 |
| T2 | **Tidak Handle Disconnected** | Tidak menangani kasus graf tidak terhubung. Solusi yang crash atau output nilai tak terdefinisi alih-alih -1. | 03, 09, 13 |
| T3 | **Overflow Integer 32-bit** | Total jarak bisa mencapai 4 × 10⁹ (4 sisi × 10⁹), melebihi batas int32 (2.147.483.647). Solusi C++ yang pakai `int` bukan `long long` akan overflow. | 08, 15 |
| T4 | **Self-loop Tidak Diabaikan** | Self-loop (u = v) seharusnya tidak mempengaruhi hasil. Implementasi yang salah mungkin menggunakan self-loop untuk "mengurangi jarak" atau error. | 06 |
| T5 | **Multi-edge Tidak Ditangani** | Antar dua simpul bisa ada banyak sisi. Solusi yang hanya menyimpan satu sisi per pasangan simpul akan salah. | 07, 16 |
| T6 | **Dijkstra O(N²) TLE** | Implementasi Dijkstra tanpa priority queue melakukan pencarian minimum secara linear O(N) setiap iterasi, menghasilkan O(N²) total. TLE pada N=100.000. | 14, 15 |
| T7 | **Greedy Lokal** | Solusi yang selalu memilih sisi terkecil saat ini (greedy lokal) bisa terperangkap pada minimum lokal dan melewatkan jalur terpendek global. | 04, 11 |
| T8 | **Relaksasi Tidak Lengkap** | Implementasi yang menghentikan relaksasi terlalu dini atau tidak memproses ulang simpul yang jaraknya diperbarui. | 10, 11 |

## 4. Tabel Test Cases

| No | File | Kategori | Ukuran (N,M) | Jebakan yang Diuji | Sumber .out | Status Validator | Status Verifikasi |
|---|---|---|---|---|---|---|---|
| 01 | 01_sample.in | SAMPLE | 4, 4 | - | brute.py | ✅ OK | ✅ PASS |
| 02 | 02_minimal_direct.in | MINIMAL | 2, 1 | T2, T6 | brute.py | ✅ OK | ✅ PASS |
| 03 | 03_minimal_disconnected.in | MINIMAL | 2, 1 | T2 (self-loop, disconnected) | brute.py | ✅ OK | ✅ PASS |
| 04 | 04_anti_bfs_trap.in | ANTI-WRONG-ANSWER | 5, 5 | T1, T7 | brute.py | ✅ OK | ✅ PASS |
| 05 | 05_anti_bfs_indirect.in | ANTI-WRONG-ANSWER | 4, 5 | T1 | brute.py | ✅ OK | ✅ PASS |
| 06 | 06_self_loop.in | EDGE | 3, 5 | T4 | brute.py | ✅ OK | ✅ PASS |
| 07 | 07_multi_edge.in | EDGE | 3, 5 | T5 | brute.py | ✅ OK | ✅ PASS |
| 08 | 08_anti_overflow.in | ANTI-OVERFLOW | 5, 4 | T3 | brute.py | ✅ OK | ✅ PASS |
| 09 | 09_disconnected.in | EDGE | 6, 4 | T2 | brute.py | ✅ OK | ✅ PASS |
| 10 | 10_linear_chain.in | EDGE | 1000, 999 | T6, T8 | brute.py | ✅ OK | ✅ PASS |
| 11 | 11_anti_greedy.in | ANTI-WRONG-ANSWER | 6, 7 | T1, T7, T8 | brute.py | ✅ OK | ✅ PASS |
| 12 | 12_random_small.in | RANDOM-KECIL | 10, 20 | T1 (acak) | brute.py | ✅ OK | ✅ PASS |
| 13 | 13_random_disconnected.in | RANDOM-KECIL | 15, 10 | T2 (acak) | brute.py | ✅ OK | ✅ PASS |
| 14 | 14_boundary_star.in | BOUNDARY/MAX | 100000, 99999 | T6 (TLE slow.py) | sol.py | ✅ OK | ✅ PASS |
| 15 | 15_max_stress.in | MAX/STRESS | 100000, 200000 | T3, T6 (TLE slow.py) | sol.py | ✅ OK | ✅ PASS |
| 16 | 16_boundary_multiedge.in | BOUNDARY/EDGE | 2, 200000 | T1, T5 (200k multi-edge) | sol.py | ✅ OK | ✅ PASS |

## 5. Hasil Validator

Semua 16 file .in divalidasi dengan `validator.py`:

```
tests/01_sample.in: OK
tests/02_minimal_direct.in: OK
tests/03_minimal_disconnected.in: OK
tests/04_anti_bfs_trap.in: OK
tests/05_anti_bfs_indirect.in: OK
tests/06_self_loop.in: OK
tests/07_multi_edge.in: OK
tests/08_anti_overflow.in: OK
tests/09_disconnected.in: OK
tests/10_linear_chain.in: OK
tests/11_anti_greedy.in: OK
tests/12_random_small.in: OK
tests/13_random_disconnected.in: OK
tests/14_boundary_star.in: OK
tests/15_max_stress.in: OK
tests/16_boundary_multiedge.in: OK
```

**Semua 16 test lolos validator.**

## 6. Hasil Verifikasi Silang (brute.py vs sol.py)

```
Cross-verifying brute.py vs sol.py on 200 random small tests...
  Test 50: OK (brute=2709393017, sol=2709393017)
  Test 100: OK (brute=825312175, sol=825312175)
  Test 150: OK (brute=1005974086, sol=1005974086)
  Test 200: OK (brute=758937445, sol=758937445)

Result: 200/200 passed, 0 mismatches
CROSS-VERIFY: LULUS semua 200 test!
```

**200/200 test acak kecil: identik antara brute (Bellman-Ford) dan sol (Dijkstra).**

## 7. Hasil run_tests.py

### sol.py — Harus PASS semua

```
PASS  : 16/16
WA    : 0
TLE   : 0
RE    : 0
✅ Semua test PASS!
```

### wrong.py — Harus gagal minimal 1

```
PASS  : 9/16
WA    : 7  (test 04, 05, 07, 11, 12, 15, 16)
✅ Syarat terpenuhi: wrong.py gagal di 7 test
```

Detail WA wrong.py (BFS unweighted):
- Test 04: expected=4, got=1000 (pilih jalur 1-hop=1000 bukan 4-hop=4)
- Test 05: expected=2, got=101 (salah hitung karena urutan BFS)
- Test 07: expected=4, got=107 (multi-edge tidak dipilih optimal)
- Test 11: expected=6, got=100 (greedy BFS terperangkap)
- Test 12: expected=44, got=105 (random acak)
- Test 15: expected=3319704229, got=5338731862 (stress test)
- Test 16: expected=813, got=115253176 (multi-edge 200k)

### slow.py — Harus TLE minimal 1

```
PASS  : 14/16
TLE   : 2  (test 14, 15)
✅ Syarat terpenuhi: slow.py TLE di 2 test
```

Detail TLE slow.py (Dijkstra O(N²)):
- Test 14: boundary_star (N=100000, M=99999) → TLE >2.0s
- Test 15: max_stress (N=100000, M=200000) → TLE >2.0s

## 8. Checker

Karena soal hanya memiliki satu jawaban benar (jarak terpendek unik atau -1), pembandingan teks sudah cukup. `checker.py` dibuat sebagai wrapper yang mem-parse integer dan membandingkan nilai, digunakan oleh `run_tests.py`.

## 9. Asumsi Eksplisit

| # | Asumsi | Alasan |
|---|---|---|
| A1 | Graf dapat memiliki komponen terhubung lebih dari dua | Soal hanya menyebut N simpul, tidak ada jaminan terhubung |
| A2 | Self-loop (u=v) tidak pernah berguna karena bobot w ≥ 1 | Bobot negatif tidak ada, self-loop tidak bisa mempersingkat jarak |
| A3 | N=2 adalah kasus minimal yang valid | Soal: 2 ≤ N |
| A4 | Simpul sumber = 1, simpul tujuan = N (bukan N-1) | Soal: "dari simpul 1 ke simpul N" |
| A5 | Bobot minimum w=1 (positif), sehingga Dijkstra valid | Soal: 1 ≤ w ≤ 10⁹ |
| A6 | Jawaban selalu unik (jarak terpendek adalah satu nilai) | Tidak ada ambiguitas — checker teks biasa cukup |

## 10. Cara Memakai untuk Solusi Sendiri

### Menguji solusi Python
```bash
cd shortest_path
python3 run_tests.py solusi_saya.py
```

### Menguji solusi C++
```bash
cd shortest_path
python3 run_tests.py solusi_saya.cpp
# Script akan otomatis kompilasi dengan g++ -O2
```

### Menguji satu test secara manual
```bash
python3 sol.py < tests/01_sample.in
# atau
python3 solusi_saya.py < tests/04_anti_bfs_trap.in
```

### Menjalankan validator pada input sendiri
```bash
python3 validator.py input_saya.in
```

### Regenerasi test (jika perlu)
```bash
python3 gen.py
# Kemudian re-generate .out:
for f in tests/*.in; do python3 sol.py < "$f" > "${f%.in}.out"; done
```

### Menambah test kustom
1. Buat file `tests/17_custom.in` sesuai format soal
2. Validasi: `python3 validator.py tests/17_custom.in`
3. Generate .out: `python3 sol.py < tests/17_custom.in > tests/17_custom.out`
4. Jalankan: `python3 run_tests.py solusi_saya.py`

## 11. Struktur File

```
shortest_path/
├── problem.md          # Deskripsi soal lengkap
├── REPORT.md           # Laporan ini
├── validator.py        # Memeriksa format & constraints input
├── brute.py            # Solusi benar lambat (Bellman-Ford O(NM))
├── sol.py              # Solusi benar cepat (Dijkstra O((N+M)logN))
├── wrong.py            # Solusi SALAH (BFS tanpa bobot)
├── slow.py             # Solusi benar tapi TLE (Dijkstra O(N²))
├── gen.py              # Generator test (seed=42)
├── checker.py          # Checker integer
├── run_tests.py        # Runner otomatis (py & cpp, TL=2s)
├── cross_verify.py     # Verifikasi silang brute vs sol (200 test)
└── tests/
    ├── 01_sample.in/out         SAMPLE
    ├── 02_minimal_direct.in/out MINIMAL
    ├── 03_minimal_disconnected.in/out MINIMAL
    ├── 04_anti_bfs_trap.in/out  ANTI-WRONG-ANSWER (T1,T7)
    ├── 05_anti_bfs_indirect.in/out ANTI-WRONG-ANSWER (T1)
    ├── 06_self_loop.in/out      EDGE (T4)
    ├── 07_multi_edge.in/out     EDGE (T5)
    ├── 08_anti_overflow.in/out  ANTI-OVERFLOW (T3)
    ├── 09_disconnected.in/out   EDGE (T2)
    ├── 10_linear_chain.in/out   EDGE (T6,T8)
    ├── 11_anti_greedy.in/out    ANTI-WRONG-ANSWER (T1,T7,T8)
    ├── 12_random_small.in/out   RANDOM-KECIL
    ├── 13_random_disconnected.in/out RANDOM-KECIL (T2)
    ├── 14_boundary_star.in/out  BOUNDARY/MAX (T6 TLE)
    ├── 15_max_stress.in/out     MAX/STRESS (T3,T6 TLE)
    └── 16_boundary_multiedge.in/out BOUNDARY/EDGE (T1,T5)
```
