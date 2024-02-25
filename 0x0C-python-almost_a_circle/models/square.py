#!/usr/bin/python3
'''Module for Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize Square instance.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Return a string representation of the square.'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        '''Get the size of the square.'''
        return self.width

    @size.setter
    def size(self, value):
        '''Set the size of the square.'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Update the attributes of the square.'''
        if args:
            self._update_with_args(*args)
        elif kwargs:
            self._update_with_kwargs(**kwargs)

    def _update_with_args(self, *args):
        '''Update attributes with positional arguments.'''
        # Map positional arguments to attribute names
        attrs = ['id', 'size', 'x', 'y']
        for i, arg in enumerate(args):
            setattr(self, attrs[i], arg)

    def _update_with_kwargs(self, **kwargs):
        '''Update attributes with keyword arguments.'''
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        '''Return a dictionary representation of the square.'''
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
