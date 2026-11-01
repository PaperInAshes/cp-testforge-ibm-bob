# Longest Increasing Subsequence

## Deskripsi
Diberikan array N bilangan bulat. Cari panjang subsequence yang **strictly increasing** terpanjang.

## Format Input
- Baris 1: satu bilangan bulat `N`
- Baris 2: `N` bilangan bulat `A[i]` dipisah spasi

## Format Output
- Satu bilangan bulat: panjang LIS (Longest Increasing Subsequence) yang strictly increasing

## Constraints
- `1 <= N <= 100000`
- `-1000000000 <= A[i] <= 1000000000`

## Batas Waktu
1 detik

## Contoh Input
```
6
5 2 8 6 3 7
```

## Contoh Output
```
3
```

## Penjelasan
Salah satu LIS yang mungkin: `[2, 3, 7]` atau `[2, 6, 7]` atau `[5, 6, 7]` — panjangnya 3.
