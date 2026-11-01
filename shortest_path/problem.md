# Shortest Path

## Deskripsi
Graf tak berarah dengan N simpul dan M sisi berbobot. Cari jarak terpendek dari simpul 1 ke simpul N. Jika tidak terhubung, cetak -1.

## Format Input
- Baris pertama: dua bilangan bulat N dan M
- M baris berikutnya: tiga bilangan bulat u, v, w (sisi antara u dan v dengan bobot w)

## Format Output
Satu bilangan bulat: jarak terpendek dari simpul 1 ke simpul N, atau -1 jika tidak terhubung.

## Constraints
- 2 ≤ N ≤ 100.000
- 1 ≤ M ≤ 200.000
- 1 ≤ u, v ≤ N
- 1 ≤ w ≤ 1.000.000.000
- Self-loop dan multi-edge diperbolehkan
- Batas waktu: 2 detik

## Contoh Input
```
4 4
1 2 5
2 4 5
1 3 1
3 4 20
```

## Contoh Output
```
10
```

## Penjelasan
Jalur terpendek: 1 → 2 → 4 dengan total jarak 5 + 5 = 10.
Jalur alternatif 1 → 3 → 4 memiliki jarak 1 + 20 = 21.
