def sequential_search(data, n, target):
    i = 0
    counter = 0
    while i < n:
        if data[i].lower() == target.lower():
            counter += 1
        i += 1
    return counter

def main():
    data = [
        "Budi", "Rahmat", "Nurul", "Bina", "Fajar",
        "Bina", "Shakira", "Nabila", "Salma", "Rony"
    ]
    
    n = len(data)

    print("Daftar Absensi Siswa:")
    print(data)

    target = input("Masukkan nama siswa yang ingin dicari: ")

    counter = sequential_search(data, n, target)

    if counter > 0:
        print(f"Nama {target} ditemukan sebanyak {counter} kali dalam absensi.")
    else:
        print(f"Nama {target} tidak ditemukan dalam absensi.")


if __name__ == "__main__":
    main()