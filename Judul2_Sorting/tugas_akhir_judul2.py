def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  
                tukar(arr, j, j + 1)

def main():
    try:
        n = int(input("Masukkan jumlah barang: "))  
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []
    print("Masukkan harga barang (Rp):")  
    for i in range(n):
        while True:
            try:
                harga = int(input(f"Harga barang {i+1}: Rp" ))  
                arr.append(harga) 
                break
            except ValueError:
                print("Input tidak valid, silahkan masukkan angka!")

    print(f"\nHarga sebelum diurutkan: {arr}")  
    bubble_sort(arr, n)
    print("Harga setelah diurutkan (termurah ke termahal):", end=" ")
    for i in range(n):
        print(f"Rp {arr[i]:,}", end="  ")
    print()
    
if __name__ == "__main__":
    main()