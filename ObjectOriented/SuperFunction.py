class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    # For a true square you can simplify __init__ to take just one side:
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


square = Square(3)
cube   = Cube(3, 3, 3)

print(square.area())  
print(cube.volume())   
