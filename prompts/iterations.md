# Iterasi Prompt 

## v1: prompt khusus Maximum Subarray
- Hasil: 15 test, validator 15/15, cross-check 200/200, wrong.py gagal 4 test.
- Masalah: test 05, 08, 09 sama-sama "semua negatif"; tidak ada bukti TLE.

## v2: prompt umum (dipakai pada Coin Change, Shortest Path, LIS, Penukaran Emas)
- Perubahan: daftar jebakan di awal, aturan keberagaman, slow.py, syarat
  wrong.py harus gagal dan slow.py harus TLE, dukungan .py dan .cpp.
- Hasil: tiap soal punya jebakan terpetakan ke test; wrong.py gagal 4-7 test.
- Masalah: pada Penukaran Emas (N<=1000) ada test kembar (jawaban 1370
  berulang), kategori ANTI-OVERFLOW dipaksakan, dan slow.py TLE hanya
  karena loop buatan.

## v3: Diskon Beli A Gratis B (solusi pengguna dipakai sebagai referensi)
- Perubahan: file solusi benar, wrong_*, dan slow dari pengguna tidak
  ditulis ulang; kategori hanya jika relevan; dilarang loop buatan.
- Hasil: 18 test; sol.cpp 18/18; wrong_overflow 6 WA; wrong_offbyone 5 WA;
  wrong_greedy_order 3 WA; slow.cpp 6 TLE alami.
- Masalah: ringkasan Bob tidak cocok dengan hasil terminal (jumlah WA/TLE
  dan deskripsi bug salah). Test kurang kuat menangkap wrong_greedy_order
  (hanya 3 dari 18).

## Perbaikan yang direncanakan (v4, belum dijalankan)
- Laporan wajib menyalin output run_tests apa adanya.
- Wajib minimal 5 test acak menengah dengan N > A+B dan sisa barang.


Bob mengikuti aturan tidak menulis ulang file pengguna, tetapi ringkasan akhirnya salah melaporkan deskripsi bug dan jumlah WA/TLE. Itu sebabnya angka diambil dari eksekusi nyata di terminal. Ini justru mendukung prinsip project: hasil harus diverifikasi lewat kode, bukan percaya narasi AI.
wrong_greedy_order.cpp hanya gagal di 3 dari 18 test (keterbatasan test acak menengah).