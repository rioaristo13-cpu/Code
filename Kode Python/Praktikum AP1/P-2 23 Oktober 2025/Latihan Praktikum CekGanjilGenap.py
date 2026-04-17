
#Melihat jika angka yang sudah diinput jika merupakan bilangan ganjil atau genap
def cek_angka_ganjilgenap(angka):         
    if angka % 2 == 0:
        return f"{angka} adalah bil. genap"
    else:
        return f"{angka} adalah bil. ganjil"

#Meminta masukan/input di terminal dari user untuk memasukkan nilai integer/angka
print("=== Program Cek Ganjil atau Genap ===")
bilangan = int(input("Masukkan Angka :"))

#Memanggil fungsi cek_angka_ganjilgenap dan mengambil nilai untuk (bilangan) dari input terminal
hasil = cek_angka_ganjilgenap(bilangan)
print(hasil)

