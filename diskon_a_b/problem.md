# Diskon Beli A Gratis B

**Batas Waktu:** 1 detik  
**Batas Memori:** 256 MB

## Deskripsi

Sebuah toko memberikan diskon spesial. Aturan diskon:

- Membeli tepat **A+B** barang: bayar hanya **A barang termahal** (B barang termurah gratis).
- Membeli **lebih dari A+B** barang: boleh membentuk **kelompok-kelompok** masing-masing berisi tepat **A+B** barang; di tiap kelompok bayar hanya **A barang termahal**.
- Tiap barang masuk **paling banyak satu kelompok**. Barang yang tidak masuk kelompok dibayar penuh.

Diberikan **N** barang dengan harga h₁, h₂, …, hₙ. Tentukan **total biaya minimum** yang harus dibayar.

## Format Input

- Baris 1: tiga bilangan bulat **N A B**
- Baris 2: N bilangan bulat h₁ h₂ … hₙ

## Format Output

Satu bilangan bulat: total biaya minimum.

## Constraints

- 1 ≤ N, A, B ≤ 100.000
- 1 ≤ hᵢ ≤ 1.000.000.000

## Contoh

### Contoh 1

**Input:**
```
5 2 1
60 100 30 75 80
```

**Output:**
```
270
```

**Penjelasan:** Urutkan descending: 100 80 75 60 30. Dengan A=2, B=1, step=3. Satu kelompok: {100, 80, 75} → bayar 100+80=180. Sisa: 60+30=90 (tidak dalam kelompok). Total = 180+90 = 270.

### Contoh 2

**Input:**
```
4 2 3
100 50 70 30
```

**Output:**
```
250
```

**Penjelasan:** A+B = 5, N=4 < 5, tidak cukup membentuk satu kelompok penuh. Semua barang dibayar penuh: 100+70+50+30 = 250.
