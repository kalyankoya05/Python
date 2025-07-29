class Car:
    def turn_on(self):
        print("you start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("Stepped on the brakes")
        return self

    def turn_off(self):
        print("engine off")
        return self


car = Car()
# car.brake()
# car.drive()
# car.turn_off()
# car.turn_on()

car.turn_on().drive().brake().turn_off()