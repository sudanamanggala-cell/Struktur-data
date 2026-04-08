nama = input("masukan nama pendek anda :")

if nama == "sudana":
    print(f"selamat datang {nama}")
else:
    print("program selesai")
    
umur = int(input("masukan umur anda :"))

if umur <= 0:
    print("anda belum lahir")
elif umur <= 18:
    print("anda belum cukup umur")
elif umur > 60:
    print("banyakin ibadah, bentar lagi mati")
elif umur >= 18:
    print("anda cukup umur")
else:
    print("program selesai")