## TUGAS AKHIR JUDUL 5 ##

**Program Leaderboard Game**

## Deskripsi Singkat ##

Program ini digunakan untuk mengelola leaderboard game dengan menggunakan struktur data binary search tree. Program ini menerapkan konsep tree yaitu data skor disusun berdasarkan nilai skor sehingga proses pencarian skor terkecil, skor terbesar, dan pengurutan skor dapat dilakukan lebih efisien. Program bekerja dengan menambahkan nama pemain dan skor, mencari skor terkecil dan terbesar, dan menampilkan seluruh data skor secara menggunakan traversal inorder. Program ini memiliki fungsi untuk menambahkan skor pemain, mencari skor terkecil dan terbesar, serta menampilkan urutan skor pemain dari yang terkecil hingga terbesar. 

## Source Code ##

<img width="1294" height="3712" alt="Source code BST" src="https://github.com/user-attachments/assets/ff6f38ba-9406-46da-96ea-5fa1b283854e" />

1.	Mendefinisikan class Node sebagai node pada program 

2.	Untuk menginisialisasi object node 

3.	Menyimpan skor pemain ke dalam atribut key 

4.	Menyimpan nama pemain ke dalam atribut nama 

5.	Membuat subpohon kiri 

6.	Membuat subpohon  kanan

7.

8.    Mendefinisikan class LeaderboardGame

9.	Untuk untuk inisialisasi object 

10.	Sebagai nilai paling atas 

11.

12.	Untuk menambahkan node 

13.	Mengecek apakah root masih kosong 

14. Jika kosong, maka dibuat node baru 

15.	Mengecek apakah skor lebih kecil dari root 

16. Jika lebih kecil, data dimasukkan ke subpohon kiri 

17.	Mengecek apakah skor lebih besar dari root

18. Jika lebih besar, data dimasukkan ke subpohon kanan 

19. Mengembalikan root 

20.

21.	Mendefinisikan fungsi insert 

22. Untuk menginputkan data baru melalui root utama 

23. 

24. Untuk mencari skor terkecil 

25. Mengecek apakah root kosong 

26. Jika kosong, mengembalikan nilai -1 

27.	Untuk menyimpan posisi node saat ini 

28.	Melakukan perulangan selama masih ada subpohon kiri 

29.	Memindahkan posisi current ke node kiri berikutnya 

30.	Mengembalikan nilai terkecil 

31.

32.	Untuk mencari skor terbesar pada 

33.	Mengecek apakah root kosong 

34.	Jika kosong, mengembalikan nilai -1 

35.	Untuk menyimpan posisi node saat ini 

36.	Melakukan perulangan selama masih ada subpohon kanan 

37. Memindahkan posisi current ke node kanan berikutnya 

38.	Mengembalikan nilai key terbesar 

39.

40. Untuk menampilkan skor dari kecil ke besar 

41.	Mengecek apakah root kosong 

42.	Jika kosong proses dihentikan 

43.	Memanggil traversal inorder pada subkiri 

44.	Menampilkan nama pemain dan skor 

45. Memanggil traversal inorder pada subkanan 

46.

47.	Mendefinisikan fungsi utama program 

48. Membuat object dari class LeaderboardGame 

49.	Menyimpan pilihan menu pengguna 

50.	Melakukan perulangan selama belum memilih menu keluar 

51. Menampilkan judul program 

52. Menampilkan menu masukkan skor 

53.	Menampilkan menu melihat skor terkecil 

54.	Menampilkan menu melihat skor terbesar 

55.	Menampilkan menu melihat urutan skor 

56.	Menampilkan menu keluar program 

57.

58. Untuk menangani kesalahan input 

59. Meminta untuk memasukkan pilihan menu 

60.	Dijalankan jika error 

61.	Menampilkan input tidak valid

62.	Kembali ke menu utama 

63.

64.	Jika memilih menu 1 

65.	Untuk menangani kesalahan input  

66.	Meminta untuk memasukkan nama 

67.	Meminta untuk memasukkan skor 

68.	Memasukkan data pemain 

69.	Menampilkan data berhasil ditambahkan 

70.	Dijalankan jika error

71.	Menampilkan input tidak valid

72.

73.	Memilih menu 2

74.	Menampilkan skor terkecil 

75.

76.	Memilih menu 3

77.	Menampilkan skor terbesar 

78.

79.	Memilih menu 4

80.	Menampilkan judul urutan skor 

81.	Menampilkan seluruh skor secara inorder 

82.	Menampilkan urutan skor

83.

84.	Memilih menu 5

85.	Menampilkan program selesai 

86.	Dijalankan jika pilihan salah

87.	Menampilkan pilihan tidak valid

88.

89.	Untuk memastikan program dijalankan langsung dari file utama 

90.	Untuk menjalankan fungsi utama

## Output Program ##

<img width="344" height="177" alt="Cuplikan layar 2026-05-26 222004" src="https://github.com/user-attachments/assets/f50af03e-55b2-4833-85a0-860cc55f05c6" />

**Menu 1**

<img width="395" height="238" alt="Cuplikan layar 2026-05-26 193604" src="https://github.com/user-attachments/assets/555dc601-e18b-40db-96be-24f540ad93f0" />

<img width="397" height="243" alt="Cuplikan layar 2026-05-26 193611" src="https://github.com/user-attachments/assets/46e5b7dd-6f41-469b-a8c5-6db48e1b9113" />

<img width="410" height="236" alt="Cuplikan layar 2026-05-26 193622" src="https://github.com/user-attachments/assets/4c63aa01-2284-457a-b8d4-005bb97daff6" />

<img width="375" height="244" alt="Cuplikan layar 2026-05-26 193628" src="https://github.com/user-attachments/assets/f8e6e685-5bd5-4627-b5e6-886492b4d3f9" />

**Menu 2**

<img width="365" height="203" alt="Cuplikan layar 2026-05-26 193635" src="https://github.com/user-attachments/assets/9be45983-07e3-4ddc-902a-46ba8552c865" />

** Menu 3**

<img width="383" height="210" alt="Cuplikan layar 2026-05-26 193642" src="https://github.com/user-attachments/assets/999b7e07-1f48-49df-9284-90adf1ab22f5" />

**Menu 4**

<img width="333" height="298" alt="Cuplikan layar 2026-05-26 193655" src="https://github.com/user-attachments/assets/308a3508-3294-4aa0-942c-507f71569387" />

**Menu 5**

<img width="329" height="187" alt="Cuplikan layar 2026-05-26 193715" src="https://github.com/user-attachments/assets/4b4cdb93-5bf7-4269-93c7-744cfb649d2a" />


**Link Youtube**

https://youtu.be/ZI2RFIt72SA
