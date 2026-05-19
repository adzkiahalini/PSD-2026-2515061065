class QueueArray:
    def __init__(self, max_size=100):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def enqueue(self, x):
        if self.is_full():
            print("Antrean penuh")
            return

        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN

        self.q[self.rear_idx] = x
        print(f"Pesanan '{x}' berhasil ditambahkan ke antrean")

    def dequeue(self):
        if self.is_empty():
            print("Antrean kosong")
            return

        print(f"Pesanan '{self.q[self.front_idx]}' sedang diproses")

        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    def peek(self):
        if self.is_empty():
            print("Antrean kosong")
            return

        print(f"Pesanan berikutnya: {self.q[self.front_idx]}")

    def display(self):
        if self.is_empty():
            print("Antrean kosong")
            return

        print("\nDaftar Antrean Pesanan:")
        i = self.front_idx
        nomor = 1

        while True:
            print(f"{nomor}. {self.q[i]}")
            if i == self.rear_idx:
                break
            i = (i + 1) % self.MAXN
            nomor += 1


def main():
    antrean = QueueArray()

    pilih = 0

    while pilih != 5:
        print("\n=== ANTREAN PESANAN RESTORAN ===")
        print("1. Tambah Pesanan")
        print("2. Proses Pesanan")
        print("3. Lihat Pesanan Terdepan")
        print("4. Tampilkan Semua Antrean")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            nama = input("Nama pelanggan: ")
            makanan = input("Pesanan makanan: ")

            pesanan = f"{nama} - {makanan}"
            antrean.enqueue(pesanan)

        elif pilih == 2:
            antrean.dequeue()

        elif pilih == 3:
            antrean.peek()

        elif pilih == 4:
            antrean.display()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()