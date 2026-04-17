while True:
    def diskon():
        nama =      input("Masukkan Nama Barang   : ")
        harga = int(input("Masukkan Harga Barang  : "))
        jumlah =int(input("Masukkan Jumlah Barang : "))
        total = harga*jumlah
        if total > 1000000:
            tdiskon = total*0.5
            dis = "50%"
        elif total > 500000:
            tdiskon = total*0.4
            dis = "40%"
        elif total > 100000:
            tdiskon = total*0.2
            dis = "20%"
        else:
            tdiskon = total
            dis = "0%"
        print (f"Nama Barang    : {nama}")
        print (f"Harga Barang   : Rp {harga}")
        print (f"Jumlah Barang  : {jumlah}")
        print (f"Total Harga    : Rp {total}")
        print (f"Harga Didiskon : Rp {total-tdiskon}")
        print (f"Diskon Harga   : {dis}\n")

    def fileuang():
        with open ("file.txt","w") as file:
            nama = input("Masukkan nama barang : ")
            harga = input("Masukkan harga barang : ")
            jumlah = input("Masukkan jumlah barang : ")
            file.write(nama+"\n")
            file.write(harga+"\n")
            file.write(jumlah+"\n")
        print ("")
    def bacauang():
        with open ("file.txt","r") as file:
            for baris in (file):
                print (baris)
    def listbarang():
        list = []
        banyak = int(input("\nBanyak barang dalam gudang: "))
        print ()

        for i in range (banyak):
            isi = input (f"Masukkan nama barang ke-{i+1}: ")
            list.append(isi)
        
        print(list,"\n")

    def main():
        print ("PROGRAM PENGATURAN KEUANGAN")
        print ("1. DISKON HARGA")
        print ("2. FILE KEUANGAN")
        print ("3. BACA FILE KEUANGAN")
        print ("4. ISI GUDANG")
        print ("5. KELUAR")
        pil = int(input("Pilih Salah Satu Menu : "))
        if pil == 1:
            diskon()
        elif pil == 2:
            fileuang()
        elif pil == 3:
            bacauang()
        elif pil == 4:
            listbarang()
        elif pil == 5:
            print("Program Selesai...")
            quit()
        else:
            print("Pilih yang ada di Menu.")
    main()