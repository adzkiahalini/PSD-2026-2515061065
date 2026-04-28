def menu():
    print("\n===== Daftar Tugas =====")
    print("1. Tampilkan semua tugas")
    print("2. Tambah tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

def main():
    tugas = []
    running = True

    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka!")
            continue

        if choice == 1:
            if len(tugas) == 0:
                print("Belum ada tugas!")
            else:
                print("\nDaftar Tugas:")
                for i in range(len(tugas)):
                    print(f"  {i+1}. {tugas[i]}")

        elif choice == 2:
            nama_tugas = input("Masukkan nama tugas: ").strip()
            if nama_tugas == "":
                print("Nama tugas tidak boleh kosong!")
            else:
                tugas.append(nama_tugas)
                print(f"Tugas '{nama_tugas}' berhasil ditambahkan!")

        elif choice == 3:
            if len(tugas) == 0:
                print("Belum ada tugas!")
            else:
                print("\nPilih tugas yang ingin dihapus:")
                for i in range(len(tugas)):
                    print(f"  {i+1}. {tugas[i]}")
                try:
                    index = int(input("Nomor tugas: ")) - 1
                    if 0 <= index < len(tugas):
                        hapus = tugas.pop(index)
                        print(f"Tugas '{hapus}' berhasil dihapus!")
                    else:
                        print("Nomor tugas tidak valid!")
                except ValueError:
                    print("Masukkan angka yang valid!")

        elif choice == 4:
            running = False
            print("Program selesai. Sampai jumpa!")

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()