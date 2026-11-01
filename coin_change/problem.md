# Coin Change

## Deskripsi
Ada N jenis koin dengan nilai C[1..N] (stok tak terbatas). Cari jumlah koin minimum agar totalnya tepat X. Jika mustahil, cetak -1.

## Input
- Baris 1: dua bilangan bulat N dan X
- Baris 2: N bilangan bulat C[i] (nilai koin, berbeda-beda)

## Output
Satu bilangan bulat: jumlah koin minimum untuk membentuk total X, atau -1 jika mustahil.

## Constraints
- 1 ≤ N ≤ 100
- 1 ≤ X ≤ 10000
- 1 ≤ C[i] ≤ 10000
- Semua nilai C[i] berbeda-beda
- Stok tiap koin tak terbatas

## Batas Waktu
1 detik

## Contoh Input
```
3 11
1 2 5
```

## Contoh Output
```
3
```

## Penjelasan
11 = 5 + 5 + 1 → 3 koin (minimum)
