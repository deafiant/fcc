class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return (("*" * self.width) + "\n") * self.height
    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

class Square(Rectangle):
    def __init__(self, side):
        self.width = self.height = side
    def set_side(self, side):
        self.width = self.height = side
    def __str__(self):
        return f"Square(side={self.width})"
    def set_width(self, width):
        self.width = self.height = width
    def set_height(self, height):
        self.height = self.width = height

if __name__ == "__main__":
    rect = Rectangle(5, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(4)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))