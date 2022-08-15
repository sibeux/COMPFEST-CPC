# Daftar Ulang

Time limit 1 s

Memory limit 64 MB

## Deskripsi

Sebentar lagi akan diadakan sebuah seminar tentang suatu algoritma baru. Karena mendatangkan narasumber yang terkenal, cukup banyak orang yang tertarik mendaftar. Faktanya, terdapat N orang yang mendaftar. Tentunya, sebelum seminar dimulai, mereka harus mendaftar ulang terlebih dahulu. Di meja pendaftaran, terdapat kertas yang berisi data pendaftar, terurut berdasarkan urutan pendaftaran mereka sebelum ini. Saat ini, ada Q orang yang mengantri untuk daftar ulang. Tentunya, untuk kelancaran pendaftaran, anda harus dapat memberi tahu nomor urut setiap orang dengan cepat. Nomor urut merupakan urutan pendaftaran mereka. Namun, dalam antrian tersebut juga ada beberapa orang yang belum mendaftar, namun berharap bisa menyelinap masuk (jangan ditiru!). Untuk setiap orang dalam antrian, mampukah anda menentukan nomor urut mereka?

## Format Masukan

Baris pertama 2 buah bilangan bulat N dan Q, masing-masing menyatakan banyak pendaftar dan banyak orang yang mengantri.

N baris selanjutnya berisi nama-nama pendaftar, terurut berdasarkan urutan pendaftaran.

Q baris selanjutnya berisi nama-nama orang yang mengantri, terurut berdasarkan urutan antrian.

## Format Keluaran

Untuk setiap orang yang mengantri, keluarkan satu baris berisi nomor urutnya jika namanya terdapat pada data pendaftar, atau "-1" (tanpa tanda petik) jika tidak ada.

## Contoh Masukan

    4 2
    dengklek
    chanek
    ganesh
    blangkon
    chanek
    ganesha

## Contoh Keluaran

    2
    -1

## Batasan

- 1 ≤ N, Q ≤ 100
- Nama setiap pendaftar maupun orang yang mengantri panjangnya tidak akan melebihi 10 karakter, dan hanya terdiri dari karakter 'a' sampai 'z'.
- Nama setiap pendaftar unik.
