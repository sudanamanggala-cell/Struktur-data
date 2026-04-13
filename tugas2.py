NAMA_BENAR = "sudana" 

while True:
    nama_input = input("Masukan nama anda : ")
    
    if nama_input == NAMA_BENAR:
        break
    else:
        print("silahkan coba lagi")

print("\n=== Selamat Datang! ===")

try:
    angka = int(input("Masukkan angka: "))
    
    print(f"Tabel Perkalian untuk {angka}:")
    for i in range(1, 11):
        hasil = angka * i
        print(f"{angka} x {i} = {hasil}")

except ValueError:
    print("Error: Harap masukkan angka yang valid.")
