import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getWidth(self):
        return self.width

    def getLength(self):
        return self.length

    def perimeter(self):
        p = (self.length*2) + (self.width*2)
        return p

    def area(self):
        a = self.width*self.length
        return a

    def diagonal(self):
        d = math.sqrt(self.length**2 + self.width**2)
        return d

def main():
    w = 7
    l = 3
    rectangle = Rectangle(w,l)
    print(rectangle.getLength(), rectangle.getWidth(), rectangle.perimeter(), rectangle.area(), rectangle.diagonal())

main()



