class Animal:

    def eat(self):
        print("Eating")


class Rabbit(Animal):

    def eat(self):
        print("rabbit eating") 

Rabbit = Rabbit()
Rabbit.eat()