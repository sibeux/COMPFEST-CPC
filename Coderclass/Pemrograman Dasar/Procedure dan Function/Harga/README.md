# Mengurutkan Harga

| Time limit | 1 s |
| --- | --- |
| Memory limit | 64 MB |

## Deskripsi

Di toko kelontong milik keluarga anda, terdapat N barang, dengan harga barang ke-i bernilai Ai. Anda diminta untuk mengurutkan barang-barang tersebut, terurut menaik sesuai harganya. Untuk melakukannya, anda membuat program. Agar anda bisa mendeteksi seandainya terjadi kesalahan, anda pun memberikan perintah yang mempermudah debugging. Akhirnya, program anda memiliki alur seperti berikut:

    for i := 1 to N
        for j := i+1 to N
            if Ai > Aj
                swap(Ai, Aj)
                println "i j"

Tentukanlah hasil keluaran program anda tersebut!

## Format Masukan

Baris pertama berisi sebuah bilangan bulat N, banyak barang di toko kelontong.

Baris selanjutnya berisi N buah bilangan bulat Ai, harga tiap barang di toko kelontong.

## Format Keluaran

Beberapa baris, hasil keluaran program yang anda buat.

## Contoh Masukan

    4
    3 2 4 1

## Contoh Keluaran

    1 2
    1 4
    2 4
    3 4

## Batasan

- 1 ≤ N ≤ 100
- 1 ≤ Ai ≤ 100
