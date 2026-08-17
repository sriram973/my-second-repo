class Rectangle:
    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.length = length
    def surface_area(self):
        return 2 * (self.width * self.height + self.width * self.length + self.height * self.length)
    def volume(self):
        return self.width * self.height * self.length
r1 = Rectangle(5, 10, 15)
print(r1.surface_area())
print(r1.volume())