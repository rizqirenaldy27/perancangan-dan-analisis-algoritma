import os

def proses_segitiga():
    header = """
+=======================================+
| NIM: 2411600477                       |
| Nama: Rizqi Renaldy Ahmad Faiz        |
| Program untuk mencetak jenis segitiga |
| dari tiga panjang sisi yang diinput   |
+=======================================+
    """
    print(header)

    bilangan = list(map(int, input("Input Panjang 3 Sisi (pisahkan dengan spasi): ").split()))
    
    if len(bilangan) != 3:
        print("Harap masukkan tepat 3 angka.")
        return

    for i, angka in enumerate(bilangan, start=1):
        print(f"Sisi {i}: {angka}")
    
    # Cek jenis segitiga
    if sum(bilangan) > 2 * max(bilangan):
        unique_sides = len(set(bilangan))
        if unique_sides == 1:
            print("Segitiga Sama Sisi")
        elif unique_sides == 2:
            print("Segitiga Sama Kaki")
        else:
            print("Segitiga Sembarang")
    else:
        print("Bukan Segitiga")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    proses_segitiga()
    
    if input("Lanjut? (y/n): ").lower() != 'y':
        break
