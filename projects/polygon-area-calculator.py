class Rectangle:
    width = 0
    height = 0

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
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        width, height = self.width, self.height
        picture = ""

        if width > 50 or height > 50:
            return "Too big for picture."

        for line in range(height):
            picture += width * "*" + "\n"

        return picture

    def get_amount_inside(self, shape):
        return int(self.height * self.width / (shape.height * shape.width))


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height

    def __str__(self):
        return f"Square(side={self.height})"
