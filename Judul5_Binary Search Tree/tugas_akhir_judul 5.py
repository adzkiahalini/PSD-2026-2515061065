class Node:
    def __init__(self, key, nama):
        self.key = key
        self.nama = nama
        self.left = None
        self.right = None

class LeaderboardGame:  
    def __init__(self):
        self.root = None

    def insert_node(self, root, key, nama):
        if root is None:
            return Node(key, nama)
        if key < root.key:
            root.left = self.insert_node(root.left, key, nama)
        elif key > root.key:
            root.right = self.insert_node(root.right, key, nama)
        return root

    def insert(self, key, nama):
        self.root = self.insert_node(self.root, key, nama)

    def find_min(self, root):
        if root is None:
            return -1
        current = root
        while current.left is not None:
            current = current.left
        return current.key
    
    def find_max(self, root):
        if root is None:
            return -1
        current = root
        while current.right is not None:
            current = current.right
        return current.key

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(f"{root.nama} : {root.key}")
        self.inorder(root.right)

def main():
    bst = LeaderboardGame() 
    pilih = 0
    while pilih != 5:  
        print("\n=== Leaderboard Game ===")
        print("1. Masukkan skor")
        print("2. Skor terkecil")
        print("3. Skor terbesar")
        print("4. Urutan skor")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                nama = input("Masukkan nama: ")
                key = int(input("Masukkan skor: "))
                bst.insert(key, nama)
                print("Data berhasil ditambahkan")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            print(f"Skor terkecil: {bst.find_min(bst.root)}")

        elif pilih == 3:
            print(f"Skor terbesar: {bst.find_max(bst.root)}")

        elif pilih == 4:
            print("Urutan skor: ")
            bst.inorder(bst.root)
            print()

        elif pilih == 5:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()