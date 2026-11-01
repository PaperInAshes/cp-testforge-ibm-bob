# Penukaran Emas

**Time limit:** 1 s  
**Memory limit:** 16 MB

## Deskripsi

Tetangga Pak Dengklek baru saja membuka usaha toko emas. Toko emas tersebut melayani jual, beli, dan tukar emas. Uniknya, proses penukaran emas pada toko tersebut adalah sebagai berikut. Satu keping emas dengan berat N gram dapat ditukar dengan tiga keping emas dengan berat masing-masing N/2, N/3, dan N/4. Jika nilai N/2, N/3, N/4 tersebut tidak bulat, maka nilainya akan dibulatkan ke bawah.

Pak Dengklek yang cerdik tampaknya menemui celah sistem penukaran tersebut, ia tahu bahwa untuk beberapa nilai N, dengan satu atau lebih proses penukaran, ia mungkin memperoleh total berat emas yang lebih besar daripada semula. Bantulah Pak Dengklek memperkirakan total berat emas maksimum yang dapat ia peroleh jika ia memiliki modal sekeping emas dengan berat N (10 ≤ N ≤ 1.000) gram.

## Format Masukan

Baris pertama berisi sebuah bilangan bulat N.

## Format Keluaran

Sebuah baris berisi sebuah bilangan bulat yaitu berat emas maksimum yang dapat Pak Dengklek peroleh.

## Contoh Masukan 1

```
12
```

## Contoh Keluaran 1

```
13
```

## Contoh Masukan 2

```
11
```

## Contoh Keluaran 2

```
11
```

## Penjelasan

Untuk N=12:
- Tukar 12 → tiga keping: 12/2=6, 12/3=4, 12/4=3. Total = 6+4+3 = 13. ✓

Untuk N=11:
- Tukar 11 → tiga keping: 11/2=5, 11/3=3, 11/4=2. Total = 5+3+2 = 10 < 11.
- Tidak menguntungkan untuk menukar, jadi tetap 11. ✓
