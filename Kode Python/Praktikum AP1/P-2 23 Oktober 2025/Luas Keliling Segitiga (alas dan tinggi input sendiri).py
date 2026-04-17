print("Masukkan Nilai Sisi a Segitiga:")
a = float(input())
print("Masukkan Nilai Sisi b Segitiga:")
b = float(input())
print("Masukkan Nilai Sisi c Segitiga:")
c = float(input())
print("Masukkan Nilai Sisi alas Segitiga:")
alas = float(input())
print("Masukkan Nilai Sisi tinggi Segitiga:")
tinggi = float(input())

def keliling (a,b,c):
    return a + b + c

def luas (tinggi, alas):
    return (1/2)*(alas*tinggi)

print (f"{keliling(a,b,c):.2f}")
print (f"{luas(tinggi,alas):.2f}")