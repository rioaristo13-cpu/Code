#Mencari Jumlah Mahasiswa Yang ingin diinput
jmahasiswa = int(input("Masukkan Jumlah Orang:"))

for i in range (jmahasiswa):
    #Memasukkan Nama Setiap Mahasiswa
    print (f"\nMahasiswa ke-{i+1}")
    nama = input("Masukkan Nama mahasiswa:")
    
    #Memasukkan Nilai UTS,UAS,Kuis
    uas = float(input("Masukkan nilai UAS:"))
    uts = float(input("Masukkan Nilai UTS:"))
    kuis = float(input("Masukkan Nilai Kuis:"))

    #Menghitung nilaitotal
    #(UTS 60%),(UAS 20%),(Kuis 20%)
    nilaitotal = (uts * 0.6)+(uas * 0.2)+(kuis * 0.2)

    #Menampilkan hasil perhitungan nilai total untuk seorang mahasiswa
    print(f"\nNilai total {nama} = {nilaitotal:.3f}")

    #Menentukan jika mahasiswa itu lulus,mungkin lulus, tidak lulus dari hasil nilaitotal
    if nilaitotal > 90:
        print("Lulus")
    elif nilaitotal > 80:
        print("Mungkin Lulus")
    elif nilaitotal > 60:
        print("Tidak Lulus")
    else:
        print("Tidak Ada")

