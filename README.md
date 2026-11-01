# CP TestForge (IBM Bob)

AI Agent berbasis IBM Bob yang mengubah soal competitive programming menjadi paket test case terverifikasi: validator, brute force, generator test, runner, serta solusi salah dan solusi lambat sebagai bukti kualitas test.

## Masalah yang diselesaikan

Soal lomba biasanya hanya menyertakan 1-3 sample, sehingga peserta sulit menguji edge case, overflow, dan batas waktu sebelum submit. CP TestForge membuat paket test yang beragam, dengan expected output yang berasal dari **eksekusi kode (brute force)**, bukan tebakan AI.

## Cara pakai

1. Buka folder ini di IBM Bob, mode **Agent**.
2. Buka `prompts/prompt_v3.md`, ganti bagian `# SOAL` dengan soal yang ingin diuji.
3. Tempel ke chat Bob (New task), lalu klik **Approve** sampai selesai.
4. Taruh kodemu di folder soal, lalu jalankan:

```bash
cd nama_folder_soal
python3 run_tests.py kodeku.cpp    # atau kodeku.py
```

Hasilnya PASS / WA / TLE / RE per test.

## Struktur repo

```
prompts/        system prompt, prompt v2, prompt v3, iterations.md
inputs/         user story
outputs/        ringkasan test case
screenshots/    bukti pengujian
max_subarray/, coin_change/, shortest_path/,
longest_increasing_subsequence/, penukaran_emas/, diskon_a_b/
                paket test hasil Bob (gen.py, validator.py, brute.py, sol, wrong, slow, tests/, REPORT.md)
```

## Soal yang diuji

| Soal | Prompt | Inti jebakan |
|---|---|---|
| Maximum Subarray | v1 | semua negatif, overflow |
| Coin Change | v2 | greedy salah |
| Shortest Path | v2 | BFS tanpa bobot, graf tidak terhubung |
| Longest Increasing Subsequence | v2 | strict vs non-strict, O(N^2) |
| Penukaran Emas | v2 | rekursi, memoization |
| Diskon Beli A Gratis B | v3 | overflow, off-by-one, urutan greedy, O(N^2) |

## Bukti Pengujian

### Struktur folder dan prompt
![Folder dan prompt](screenshots/01_folder_struktur_dan_prompt.png)

### Soal 1: Maximum Subarray (prompt v1)
![Ringkasan Bob](screenshots/02_maxsubarray_ringkasan_bob.png)
![sol.py lolos](screenshots/03_maxsubarray_sol_pass.png)
![wrong.py gagal](screenshots/04_maxsubarray_wrong_fail.png)

### Soal 2: Coin Change (prompt v2)
![Coin Change](screenshots/05_coinchange_ringkasan_bob.png)

### Soal 3: Penukaran Emas (prompt v2, diuji dengan kode C++ sendiri)
![Penukaran Emas](screenshots/06_penukaran_emas_cpp_pass.png)

### Soal 4: Diskon Beli A Gratis B (prompt v3)

Solusi benar lolos semua test:

![sol.cpp](screenshots/07_diskon_sol_pass.png)

Solusi salah tertangkap test:

![overflow](screenshots/08_diskon_wrong_overflow.png)
![off-by-one](screenshots/09_diskon_wrong_offbyone.png)
![greedy order](screenshots/10_diskon_wrong_greedy_order.png)

Solusi lambat kena TLE, dan cross-verify 200 trial tanpa mismatch:

![TLE](screenshots/11_diskon_slow_tle.png)
![TLE dan cross-verify](screenshots/12_diskon_slow_tle_dan_crossverify.png)

## Tabel Hasil Final (Diskon A-B)

| Solusi | PASS | Gagal | Test yang gagal |
|---|---|---|---|
| sol.cpp | 18 | 0 | - |
| wrong_overflow.cpp | 12 | 6 WA | 07, 09, 14, 15, 17, 18 |
| wrong_offbyone.cpp | 13 | 5 WA | 04, 05, 15, 16, 18 |
| wrong_greedy_order.cpp | 15 | 3 WA | 01, 14, 17 |
| slow.cpp (O(N^2)) | 12 | 6 TLE | 09, 14, 15, 16, 17, 18 |
| Cross-verify brute vs sol | 200 trial | 0 mismatch | - |

## Keterbatasan

- Satu `wrong` solution hanya mewakili satu jenis bug.
- `wrong_greedy_order` hanya gagal di 3 dari 18 test, artinya test acak menengah perlu diperkuat.
- Ringkasan akhir Bob pernah tidak cocok dengan hasil terminal, sehingga angka di laporan ini diambil dari eksekusi `run_tests.py` secara langsung.
- `.out` untuk test besar berasal dari solusi efisien buatan Bob/pengguna, diverifikasi silang dengan brute force pada test acak kecil.

## Potensi pengembangan

Checker untuk soal dengan banyak jawaban benar, generator test acak menengah yang lebih kuat, ekspor ke format Codeforces/Polygon, dan integrasi CI.