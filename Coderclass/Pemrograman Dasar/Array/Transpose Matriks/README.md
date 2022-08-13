# Transpose Matriks

Time limit 1 s

Memory limit 64 MB

## Deskripsi

Untuk suatu matriks A berukuran N*M, AT atau transpose matriks, merupakan hasil penukaran baris dan kolom dari matriks A. Secara formal,

[AT]ij = [A]ji

Sehingga, AT pasti berukuran M*N. Diberikan suatu matriks A, buatlah program yang dapat membuat  transposnya!

## Format Masukan

Baris pertama berisi 2 buah bilangan bulat, N dan M, masing-masing menyatakan banyak baris dan kolom matriks A.

Baris kedua sampai N+1 masing-masing berisi M buah bilangan, dimana bilangan pada baris i kolom j menyatakan A(i-1)j.

## Format Keluaran

M baris dengan masing-masing baris berisi N buah bilangan, yang menyatakan AT. Pisahkan setiap bilangan dalam baris yang sama menggunakan spasi.

## Contoh Masukan

    2 3
    1 3 4
    5 1 2

## Contoh Keluaran

    1 5
    3 1
    4 2

## Batasan

- 1 ≤ N, M ≤ 100
- 1 ≤ Aij ≤ 100
