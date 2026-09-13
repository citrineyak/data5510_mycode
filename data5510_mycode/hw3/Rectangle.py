class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calc_area(self):
        area = self.length * self.width
        return area

mr_rectangle = Rectangle(5,3)

print("area:", mr_rectangle.calc_area())