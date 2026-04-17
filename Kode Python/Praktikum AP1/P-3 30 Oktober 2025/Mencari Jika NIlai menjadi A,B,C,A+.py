#Masukkan nilai yang ingin diskor
nilai = int(input("Masukkan Nilai:"))

#Mengubah nilai menjadi alfabet
if nilai < 60:
    print ("C")
elif nilai < 80:
    print ("B")
elif nilai < 90:
    print ("A")
else:
    print ("A+")