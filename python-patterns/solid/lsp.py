class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def test_area_should_be_equal(shape):
    w = shape.width
    shape.height = 10
    expected = int(w * 10)

    print(f'Expected area of {expected}, got {shape.area}')


rc = Rectangle(2, 3)
test_area_should_be_equal(rc)

sq = Square(5)
test_area_should_be_equal(sq)

