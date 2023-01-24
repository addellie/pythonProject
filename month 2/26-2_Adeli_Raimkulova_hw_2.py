class Figure:
    unit = 'cm'

    def __init__(self, perimeter=0):
        self.__perimeter = perimeter

    @property
    def perimeter(self):
        return self.__perimeter

    @perimeter.setter
    def perimeter(self, value):
        self.__perimeter = value

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def info(self):
        pass


class Square(Figure):

    def __init__(self, side_length):
        super(Square, self).__init__(perimeter=0)
        self.__side_length = side_length
        self.__perimeter = super().calculate_perimeter()

    def calculate_area(self):
        super().calculate_area()
        return self.__side_length**2

    def calculate_perimeter(self):
        super().calculate_perimeter()
        return self.__side_length*2

    def info(self):
        super().info()
        print(f'Square side length: {self.__side_length}{Figure.unit}, '
              f'perimeter: {self.calculate_perimeter()}{Figure.unit},area: {self.calculate_area()}{Figure.unit}.')


class Rectangle(Figure):
    def __init__(self, length, width):
        super(Rectangle, self).__init__(perimeter=0)
        self.__length = length
        self.__width = width
        self.__perimeter = super().calculate_perimeter()

    def calculate_area(self):
        super().calculate_area()
        return self.__length * self.__width

    def calculate_perimeter(self):
        super().calculate_perimeter()
        return self.__length + self.__width

    def info(self):
        super().info()
        print(f'Rectangle length: length {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit}, '
              f'perimeter: {self.calculate_perimeter()}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}.')


abcd_square = Square(4)
efgh_square = Square(19)
absd_rectangle = Rectangle(12, 4)
efgh_rectangle = Rectangle(6, 2)
dsba_rectangle = Rectangle(8, 6)

figure = [absd_rectangle, efgh_rectangle, dsba_rectangle, abcd_square, efgh_square]

for i in figure:
    i.info()
