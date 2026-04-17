class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def set_balance(self, amount):
        if amount >= 0 :
            self.__balance = amount
        else:
            quit("Saldo tidak boleh negatif!")
            
nama = input("Masukkan nama pemilik Akun : ")
account = BankAccount(nama, 1000)
print(f"Pemilik : {account.owner}")
print(f"Balance : {account.get_balance()}")

while True:
    try:
        bbaru = int(input("\nMasukkan balance baru : "))
        account.set_balance(bbaru)
        break
    except Exception as a:
        print ("Input harus angka bulat positif")

print(f"\nPemilik      : {account.owner}")
print(f"Balance Baru : {account.get_balance()}")
