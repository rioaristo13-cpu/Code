def buat_file():
    try:
        with open("act4.txt", "w") as file:
            nama = input("\nMasukkan Nama : ")
            kelas = input("Masukkan Kelas : ")
            npm = input("Masukkan NPM : ")
            ujian1 = int(input("Masukkan UTS : "))
            ujian2 = int(input("Masukkan UAS : "))
            total = ((ujian1*0.4) + (ujian2*0.6)) / 2
            tb = f"{total:.2f}"

            file.write("Nama Anda : " + nama + "\n")
            file.write("Kelas Anda : " + kelas + "\n")
            file.write("NPM Anda : " + npm + "\n")
            file.write("Total Ujian : " + tb + "\n")
            file.write("\n")
        print("File 'act4.txt' berhasil dibuat dan ditulis.\n")
    except ValueError:
        print("Terjadi kesalahan: Nilai ujian harus berupa angka.")

def baca_file():
    try:
        with open("act4.txt", "r") as file:
            print("\n=== Isi File act4.txt ===")
            for baris in file:
                print (baris.strip())
    except FileNotFoundError:
        print("File tidak ditemukan. Jalankan dulu fungsi buat file().")

def main():
    while True:
        print("\n=== MENU PROGRAM FILE & EKSESPSI")
        print("1. Buat file")
        print("2. Baca file")
        print("3. Keluar")
        pilihan = int(input("Pilihan menu (1-3): "))
        if pilihan == 1:
            buat_file()
        elif pilihan == 2:
            baca_file()
        elif pilihan == 3:
            print("Program selesai. Terima kasih, Aristo!")
            break
        else:
            print("Pilihan tidak valid. Silahkan Pilih 1-3.")
main()