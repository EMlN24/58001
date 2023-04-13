class Circle:
    def __init__(self, rad, pi):
        self.rad = rad
        self.pi = pi

    def perimeter(self):
        return 2 * self.pi * self.rad

    def area(self):
        return self.pi * self.rad ** 2

    def display(self):
        print("The area of the circle is", self.area())
        print("The perimeter of the circle is", self.perimeter())

circle = Circle(float(input("Enter the radius of the circle: ")), 3.14159)
circle.display()