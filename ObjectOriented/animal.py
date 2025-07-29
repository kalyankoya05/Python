class Animal:
    alive = True

    def eat(self):
        print("The animal is eating")

    def sleep(self):
        print("The animal is sleeping")


class Rabbit(Animal):
    def run(self):
        print("The rabbit is running")

class Fish(Animal):
    def swim(self):
        print("Fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("Flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.run()
fish.swim()
hawk.fly()