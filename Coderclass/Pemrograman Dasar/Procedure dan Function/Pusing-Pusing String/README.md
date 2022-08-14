# Pusing-Pusing String

| Time limit | 1 s |
| --- | --- |
| Memory limit | 64 MB |

## Deskripsi

Setelah sukses dengan detektor palindrom, kali ini Budi mencoba membuat alat baru yang dapat memanipulasi suatu string. Alat baru ini akan menerima suatu string S, dan memiliki 2 fungsi:

1. Diberikan A dan B, menukar karakter ke-A dan ke-B.
2. Diberikan L dan R, membalik substring pada rentang [L,R]. Sebagai contoh, jika S = "abcd", L = 1, dan R = 4, maka S' = "dcba".

Perhatikan bahwa disini indeks dimulai dari 1, dan hasil operasi-operasi tersebut bersifat permanen. Untuk mengetesnya, Budi akan melakukan Q buah operasi. Untuk mengetahui kebenaran alat yang Budi buat, ia meminta anda untuk mencari tahu hasil Q buah operasi tersebut. Bantulah Budi!

## Format Masukan

Baris pertama berisi dua buah bilangan bulat, N dan Q, masing-masing menyatakan panjang string dan banyak operasi.

Baris kedua berisi sebuah string S, yang memiliki panjang N.

Q baris berikutnya berisi salah satu dari dua operasi berikut:

- 1 A B, yang menyatakan operasi menukar karakter.
- 2 L R, yang menyatakan operasi membalik substring.

## Format Keluaran

Satu baris berisi sebuah string hasil semua operasi tersebut pada S.

## Contoh Masukan

    5 2
    abcde
    1 1 2
    2 1 5

## Contoh Keluaran

    dcab

## Batasan

- 2 ≤ N ≤ 1.000
- 1 ≤ Q ≤ 1.000
- 1 ≤ A < B ≤ N
- 1 ≤ L < R ≤ N
