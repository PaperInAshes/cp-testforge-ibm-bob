## Bukti Pengujian (Soal: Diskon Beli A Gratis B)

Prompt yang dipakai (prompt v3):
![Prompt](screenshots/01_folder_dan_prompt.png)

Ringkasan akhir dari IBM Bob:
![Ringkasan Bob](screenshots/02_ringkasan_bob_diskon.png)

Solusi benar lolos semua test (18/18):
![sol PASS](screenshots/03_sol_pass.png)

Solusi salah tertangkap test:
![wrong overflow](screenshots/04_wrong_overflow.png)
![wrong offbyone](screenshots/05_wrong_offbyone.png)
![wrong greedy order](screenshots/06_wrong_greedy_order.png)

Solusi lambat kena TLE dan cross-verify 200 trial, 0 mismatch:
![slow dan cross-verify](screenshots/07_slow_tle_dan_crossverify.png)

## Hasil Soal Lain
![Coin Change](screenshots/08_coin_change_hasil.png)
![Penukaran Emas C++ PASS](screenshots/09_penukaran_emas_cpp_pass.png)

## Tabel Hasil Final (Diskon A-B)

| Solusi | PASS | Gagal | Test yang gagal |
|---|---|---|---|
| sol.cpp | 18 | 0 | - |
| wrong_overflow.cpp | 12 | 6 WA | 07, 09, 14, 15, 17, 18 |
| wrong_offbyone.cpp | 13 | 5 WA | 04, 05, 15, 16, 18 |
| wrong_greedy_order.cpp | 15 | 3 WA | 01, 14, 17 |
| slow.cpp (O(N^2)) | 12 | 6 TLE | 09, 14, 15, 16, 17, 18 |
| Cross-verify brute vs sol | 200 trial | 0 mismatch | - |