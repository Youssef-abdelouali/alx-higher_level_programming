#!/usr/bin/python3
'''Module for Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize Rectangle instance.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Get width of the rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set width of the rectangle.'''
        self.validate_dimension(value, "width")
        self.__width = value

    @property
    def height(self):
        '''Get height of the rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set height of the rectangle.'''
        self.validate_dimension(value, "height")
        self.__height = value

    @property
    def x(self):
        '''Get x-coordinate of the rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Set x-coordinate of the rectangle.'''
        self.validate_coordinate(value, "x")
        self.__x = value

    @property
    def y(self):
        '''Get y-coordinate of the rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Set y-coordinate of the rectangle.'''
        self.validate_coordinate(value, "y")
        self.__y = value

    def validate_dimension(self, value, name):
        '''Validate dimensions (width/height).'''
        if not isinstance(value, int):
            raise TypeError(f"{name.capitalize()} must be an integer.")
        if value <= 0:
            raise ValueError(f"{name.capitalize()} must be a positive integer.")

    def validate_coordinate(self, value, name):
        '''Validate coordinates (x/y).'''
        if not isinstance(value, int):
            raise TypeError(f"{name.capitalize()} coordinate must be an integer.")
        if value < 0:
            raise ValueError(f"{name.capitalize()} coordinate must be a non-negative integer.")

    def area(self):
        '''Compute the area of the rectangle.'''
        return self.width * self.height

    def display(self):
        '''Print a visual representation of the rectangle.'''
        print("\n" * self.y + (" " * self.x + "#" * self.width + "\n") * self.height, end="")

    def __str__(self):
        '''Return a string representation of the rectangle.'''
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        '''Update the attributes of the rectangle.'''
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''Return a dictionary representation of the rectangle.'''
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}
