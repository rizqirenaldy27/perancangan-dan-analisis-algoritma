def proses_bilangan():
    header = """
+=====================================+
| NIM: 2411600477                     |
| Nama: Rizqi Renaldy Ahmad Faiz      |
| Program untuk mencetak nilai tengah |
| dari tiga buah nilai yang diinput   |
+=====================================+
    """
    print(header)

    bilangan = list(map(int, input("Input 3 angka: ").split()))
    
    if len(bilangan) == len(set(bilangan)):
        bilangan = sorted(bilangan)
        _, tengah, _ = bilangan

        for angka in bilangan:
            print(f"Angka: {angka}")

        print(f"Nilai Tengah: {tengah}")
    else:
        print("Angka tidak boleh sama.")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    proses_bilangan()
    
    if input("Lanjut? (y/n): ").lower() != 'y':
        break
