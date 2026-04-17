class Saya:
    def __init__(self, nama):
        self.__nama = nama

    def get_nama(self):
        return self.__nama 

    def set_nama(self, namabaru):
        self.__nama = namabaru

nama = input("Nama Pertama : ")
saya = Saya(nama)
namabaru = input("Nama Baru : ")
saya.set_nama(namabaru)
print(f"Nama Sebelumnya : {nama}, Nama Baru : {saya.get_nama()}")