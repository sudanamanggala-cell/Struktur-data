while True:
    try:
        angka = int(input("Masukkan angka: "))
        if angka < 0:
            print("Harus positif!")
        else:
            print("angka benar")
            break
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")

print("Angka yang dimasukkan:", angka)
