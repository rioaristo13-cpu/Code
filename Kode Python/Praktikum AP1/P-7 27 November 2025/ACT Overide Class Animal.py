class Animal:
    def eat(self):
        print("Hewan sedang makan!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

kucing = Cat()
kucing.eat()
kucing.meow()