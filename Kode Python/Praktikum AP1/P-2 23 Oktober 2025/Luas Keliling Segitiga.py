import math

print("Masukkan Nilai Sisi a Segitiga:")
a = float(input())
print("Masukkan Nilai Sisi b Segitiga:")
b = float(input())
print("Masukkan Nilai Sisi c Segitiga:")
c = float(input())

def segitiga(x,b,c):
    kel = x + b + c
    s = (x + b + c) / 2
    luas = math.sqrt(max(0.0, s * (s - x) * (s - b) * (s - c)))
    print(f"Keliling segitiga: {kel:.2f}")
    print(f"Luas segitiga: {luas:.2f}")

segitiga(a, b, c)