#Latihan Praktikum
nama    =       input("Masukkan Nama Lengkap    :")
kelas   =       input("Masukkan Kelas           :")
npm     =   int(input("Masukkan NPM             :")) 
umur    =   int(input("Masukan Umur             :"))
hobi    =       input("Masukkan Hobi            :")
nuts    = float(input("Nilai UTS                :")) #
nuas    = float(input("Nilai UAS                :")) #NILAI_NILAI
nkuis   = float(input("Nilai Kuis               :")) #

#MENGHITUNG RATA RATA NILAI UTS,UAS,KUIS
rata_rata = (nuts+nuas+nkuis)/3      

#Output
print("\n=== HASIL BIODATA ===")
print("Nama                     :", nama)
print("Kelas                    :", kelas)
print("NPM                      :", npm)
print("Hobi                     :", hobi)
print("Nilai UTS                :", round(nuts ,2))   
print("Nilai UAS                :", round(nuas ,2))
print("Nilai Kuis               :", round(nkuis ,2))
print("Nilai Rata - rata        :", round(rata_rata ,2))