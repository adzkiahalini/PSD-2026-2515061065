## TUGAS AKHIR JUDUL 6 ##

**Program Data Peserta PPDB**

## Deskripsi Singkat ##

Program ini digunakan untuk mengelola data pendaftaran PPDB dengan menggunakan struktur data hash map separate chaining. Program ini menerapkan konsep hashing yaitu data peserta disimpan berdasarkan hasil perhitungan hash dari nomor pendaftaran sehingga proses pencarian, penambahan, dan penghapusan data dapat dilakukan lebih efisien. Program bekerja dengan menambahkan nomor pendaftaran dan nama peserta, mencari data peserta berdasarkan nomor pendaftaran, dan menghapus data peserta yang tidak diperlukan. Program ini memiliki fungsi untuk menambahkan data peserta, mencari data berdasarkan nomor pendaftaran, menghapus data peserta, serta menampilkan seluruh data pendaftaran beserta posisi penyimpanannya dalam tabel hash.

## Source Code ##

<img width="1618" height="3294" alt="HASH MAP KODE" src="https://github.com/user-attachments/assets/f5a80fdf-73af-4e98-869f-9613ff1b0101" />

1.	Mendefinisikan class Node sebagai node untuk menyimpan data 
2.	Untuk menginisialisasi object node
3.	Menyimpan nomor pendaftaran peserta ke dalam atribut key
4.	Menyimpan nama peserta ke dalam atribut value
5.	Membuat atribut next yang digunakan untuk menunjuk node berikutnya
6.	
7.	Mendefinisikan class 
8.	Untuk menginisialisasi object
9.	Menyimpan ukuran hash table ke dalam atribut size
10.	Membuat tabel hash yang berisi nilai none
11.	
12.	Mendefinisikan fungsi hash function
13.	Mengembalikan hasil perhitungan indeks menggunakan operasi modulo
14.	
15.	Mendefinisikan fungsi insert
16.	Menghitung indeks penyimpanan menggunakan fungsi hash
17.	Menyimpan node pertama ke variabel current
18.	Melakukan perulangan selama masih ada node 
19.	Mengecek apakah key yang dicari sudah ada
20.	Jika key sudah ada maka value diperbarui
21.	Menghentikan proses karena data telah diperbarui
22.	Pindah ke node berikutnya
23.	Membuat node baru
24.	Menghubungkan node baru dengan node yang sebelumnya 
25.	Menjadikan node baru sebagai node pertama 
26.	
27.	Mendefinisikan fungsi search
28.	Menghitung indeks berdasarkan key yang dicari
29.	Menyimpan node pertama variabel current
30.	Melakukan perulangan selama node masih ada
31.	Mengecek apakah key ditemukan
32.	Jika ditemukan maka node dikembalikan 
33.	Berpindah ke node berikutnya
34.	Jika data tidak ditemukan maka mengembalikan nilai menjadi none
35.	
36.	Mendefinisikan fungsi remove key
37.	Menghitung indeks berdasarkan key yang akan dihapus
38.	Menyimpan node pertama ke variabel current
39.	Membuat variabel prev untuk menyimpan node sebelumnya
40.	Melakukan perulangan selama node masih ada
41.	Mengecek apakah key ditemukan
42.	Mengecek apakah node yang ditemukan berada di posisi pertama
43.	Jika node pertama maka digeser ke node berikutnya
44.	Jika bukan pada  node pertama 
45.	Nodee sebelumnya dihubungkan ke node setelah node yang dihapus
46.	Mengembalikan nilai true karena data berhasil dihapus
47.	Memindahkan posisi prev ke node sekarang
48.	Memindahkan posisi current ke node berikutnya
49.	Jika data tidak ditemukan, mengembalikan nilai false
50.	
51.	Mendefinisikan fungsi display.
52.	Menampilkan judul data pendaftaran PPDB.
53.	Melakukan perulangan 
54.	Menampilkan nomor indeks
55.	Menyimpan node pertama ke variabel current
56.	Melakukan perulangan selama node masih ada
57.	Menampilkan key dan value pada node
58.	Berpindah ke node berikutnya
59.	Menampilkan tulisan NULL sebagai akhir 
60.	
61.	Mendefinisikan fungsi utama program.
62.	Membuat objek HashMapSeparateChaining bernama ppdb.
63.	Menambahkan data peserta dengan nomor pendaftaran 2515001
64.	Menambahkan data peserta dengan nomor pendaftaran 2515002
65.	Menambahkan data peserta dengan nomor pendaftaran 2515003
66.	Menambahkan data peserta dengan nomor pendaftaran 2515004
67.	Menampilkan seluruh data pendaftaran.
68.	
69.	Mencari data peserta dengan nomor pendaftaran 2515002
70.	Mengecek apakah data ditemukan
71.	Jika ditemukan, menampilkan nomor pendaftaran dan nama peserta
72.	Jika tidak ditemukan
73.	Menampilkan pesan bahwa data tidak ditemukan
74.	
75.	Menghapus data peserta dengan nomor pendaftaran 2515004
76.	Menampilkan seluruh data pendaftaran setelah ada data yang dihapus
77.	
78.	Memastikan program dijalankan langsung dari file utama
79.	Untuk menjalankan fungsi utama

## Output Program ##

**Menampilkan seluruh data peserta**

<img width="475" height="252" alt="Cuplikan layar 2026-06-09 211142" src="https://github.com/user-attachments/assets/02589098-9cda-4dd2-8f4d-2401b878d59c" />

**Mencari nomor pendaftaran**

<img width="610" height="40" alt="Cuplikan layar 2026-06-09 211148" src="https://github.com/user-attachments/assets/9c819f26-fd64-423d-b592-4be416b0a5e9" />

**Menampilkan seluruh data setelah ada data yang dihapus**

<img width="381" height="243" alt="Cuplikan layar 2026-06-09 211157" src="https://github.com/user-attachments/assets/26057fc2-26a9-4afc-9eb9-b22fb66f576b" />

**Link Youtube**

https://youtu.be/V_NEZAvF0nw
