## TUGAS AKHIR JUDUL 4 ##

**Program Antrean Pesanan di Restoran**

## Deskripsi Singkat ##

Program ini digunakan untuk mengelola antrean pesanan restoran dengan menggunakan struktur data queue berbasis array. Program ini menerapkan konsep FIFO, yaitu pesanan yang masuk lebih dahulu akan diproses lebih dahulu. Program bekerja dengan menambahkan pesanan pelanggan ke dalam antrean, memproses pesanan dari posisi terdepan, serta menampilkan pesanan yang sedang menunggu untuk diproses. Program ini memiliki fungsi untuk menambah pesanan, memproses pesanan, melihat pesanan terdepan, dan menampilkan seluruh daftar antrean pesanan. Program juga menggunakan perulangan untuk menampilkan menu secara terus-menerus sehingga pengguna dapat menjalankan beberapa proses antrean sampai pengguna memilih keluar dari program.

## Source Code ##

<img width="1370" height="4358" alt="Stack queue ss" src="https://github.com/user-attachments/assets/33299be3-b932-41ee-9c10-e898345c02a0" />

1. Mendefinisikan queue array sebagai struktur data antrean 

2. Untuk inisialisasi objek yang ada pada antrean, max_size=100 untuk menentukan kapasitas maksimum antrean

3. Menyimpan kapasitas maksimum antrean

4. Membuat list kosong sebanyak kapasitas antrean

5. Menandakan posisi depan antrean

6. Menandakan posisi belakang antrean 

7.

8. Untuk mengecek apakah antrean kosong

9. Mengembalikan nilai true jika front idx bernilai -1

10. 

11. Untuk mengecek apakah antrean penuh

12. Mengecek apakah posisi belakang sama dengan posisi depan

13.

14. Untuk menambahkan data pesanan ke antrean

15. Mengecek apakah antrean penuh 

16. Menampilkan pesan Antrean penuh jika antrean penuh

17. Untuk menghentikan proses penambahan data

18. 

19. Mengecek apakah antrean masih kosong menggunakan 

20. Jika kosong, maka front_idx berubah menjadi 0

21. Rear_idx berubah menjadi 0 

22. Jika tidak kosong

23.  Jika antrean tidak kosong, maka rear_idx ditambah satu 

24. 

25. Menyimpan data pesanan ke dalam antrean

26. Menampilkan pesanan berhasil ditambahkan ke antrean

27.

28.  Menghapus pesanan dari antrean

29. Mengecek apakah antrean kosong

30. Menampilkan Antrean kosong jika tidak ada antrean

31. Untuk menghentikan proses

32.

33. Menampilkan pesanan yang sedang diproses 

34.

35. Mengecek apakah antrean hanya memiliki satu data

36. Jika hanya satu data, maka dikembalikan menjadi -1

37. Jika data lebih dari satu, maka digeser ke data berikutnya 

38. Diijalankan jika antrean memiliki lebih dari satu data

39. Memindahkan posisi depan antrean ke data berikutnya setelah satu data diproses

40. 

41. Untuk melihat pesanan paling depan tanpa menghapus 

42. Mengecek apakah antrean kosong

43. Menampilkan Antrean kosong jika tidak ada antrean 

44. Untuk menghentikan proses. 

45.

46. Menampilkan pesanan terdepan atau selanjutnya pada antrean. 

47. 

48.  Untuk menampilkan seluruh isi antrean

49. Mengecek apakah antrean kosong

50. Menampilkan Antrean kosong jika tidak ada antrean

51. Untuk menghentikan proses

52. 

53. Menampilkan judul Daftar Antrean Pesanan

54. Variabel i untuk menyimpan posisi awal antrean

55. Variabel nomor sebagai nomor urut tampilan antrean

56. 

57. Untuk menampilkan semua data antrean

58. Menampilkan nomor antrean dan isi pesanan

59. Mengecek apakah posisi saat ini sudah sama dengan posisi belakang antrean 

60. Untuk menghentikan perulangan jika data terakhir sudah ditampilkan

61. Memindahkan indeks ke data berikutnya 

62. Menambah nomor urut antrean. 

63.

64. 

65. Mendefinisikan fungsi utama program

66. Membuat objek antrean dengan nama antrean dari class QueueArray

67. 

68. Untuk menyimpan pilihan menu pengguna

69. 

70. Melakukan perulangan selama pengguna belum memilih menu keluar

71. Menampilkan judul program ANTREAN PESANAN RESTORAN

72. Menampilkan menu tambah pesanan

73. Menampilkan menu proses pesanan

74. Menampilkan menu melihat pesanan terdepan

75. Menampilkan menu menampilkan seluruh antrean
 
76. Menampilkan menu keluar program

77. 

78. Untuk menangani kesalahan input 

79. Untuk meminta pengguna memilih menu

80. Dijalankan jika input bukan angka

81. Menampilkan pesan Input tidak valid! jika terjadi kesalahan input

82. Untuk mengulang kembali ke menu

83. 

84. Mengecek apakah pengguna memilih menu 1

85. Untuk menginput nama pelanggan 

86. Untuk menginput nama makanan

87. 

88. Menggabungkan nama pelanggan dan makanan ke dalam variabel pesanan

89. Untuk menambahkan pesanan ke antrean

90. 

91. Mengecek apakah pengguna memilih menu 2

92. Untuk memproses pesanan terdepan

93. 

94. Mengecek apakah pengguna memilih menu 3

95. Untuk melihat pesanan terdepan

96. 

97. Mengecek apakah pengguna memilih menu 4

98. Untuk menampilkan seluruh antrean

99. 

100. Mengecek apakah pengguna memilih menu 5

101. Menampilkan Program selesai

102. 

103. Diijalankan jika pilihan menu tidak tersedia

104. Menampilkan Pilihan tidak valid!

105. 

106. Untuk memastikan program dijalankan langsung

107.  Untuk menjalankan seluruh program 

## Output Program ##

<img width="372" height="136" alt="Cuplikan layar 2026-05-19 223956" src="https://github.com/user-attachments/assets/e576709e-6723-45cc-8094-6cae4709f600" />

**Menu 1**

<img width="691" height="103" alt="Cuplikan layar 2026-05-19 224005" src="https://github.com/user-attachments/assets/b9072f23-a67d-451a-aa98-b86074e2e650" />

<img width="585" height="105" alt="Cuplikan layar 2026-05-19 224011" src="https://github.com/user-attachments/assets/6218091c-8395-4865-8a0a-f6fe19260f09" />

<img width="620" height="99" alt="Cuplikan layar 2026-05-19 224019" src="https://github.com/user-attachments/assets/9ec0c89f-3d55-4c16-9125-e321aa0dc3d8" />


**Menu 2**

<img width="439" height="47" alt="Cuplikan layar 2026-05-19 224028" src="https://github.com/user-attachments/assets/33877eeb-fb35-4886-80fa-bb380d8a7bb2" />


**Menu 3**

<img width="389" height="71" alt="Cuplikan layar 2026-05-19 224033" src="https://github.com/user-attachments/assets/95ee402b-d1f6-44a7-bee3-d2259b89906d" />


**Menu 4**

<img width="272" height="117" alt="Cuplikan layar 2026-05-19 224042" src="https://github.com/user-attachments/assets/493d4504-58cf-4bb1-ad40-dda53d6347d5" />


**Menu 5**

<img width="216" height="49" alt="Cuplikan layar 2026-05-19 224058" src="https://github.com/user-attachments/assets/5bbb67a6-626e-4439-a0d9-1578862041ef" />


**Link Youtube**

https://youtu.be/xIkTIxrPp5Q
