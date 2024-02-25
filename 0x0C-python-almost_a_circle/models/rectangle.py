#!/usr/bin/python3
'''Module for Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Width of this rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_dimension(value, "width")
        self.__width = value

    @property
    def height(self):
        '''Height of this rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_dimension(value, "height")
        self.__height = value

    @property
    def x(self):
        '''x of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_coordinate(value, "x")
        self.__x = value

    @property
    def y(self):
        '''y of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_coordinate(value, "y")
        self.__y = value

    def validate_dimension(self, value, name):
        '''Method for validating dimensions.'''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be a positive integer")

    def validate_coordinate(self, value, name):
        '''Method for validating coordinates.'''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

    def area(self):
        '''Computes area of this rectangle.'''
        return self.width * self.height

    def display(self):
        '''Prints string representation of this rectangle.'''
        rectangle_representation = '\n'.join([' ' * self.x + '#' * self.width for _ in range(self.y, self.y + self.height)])
        print(rectangle_representation)

    def __str__(self):
        '''Returns string info about this rectangle.'''
        return f'[{type(self).__name__}] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}'

    def __update(self, **kwargs):
        '''Internal method that updates instance attributes via keyword args.'''
        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.'''
        if args:
            keys = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, keys[i], value)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
