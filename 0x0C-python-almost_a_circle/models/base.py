#!/usr/bin/python3

'''Base class module.'''

from json import dumps, loads
import csv
import turtle
import time
from random import randrange


class Base:
    '''An illustration of the foundation 
    of our Object-Oriented Programming hierarchy.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Converts a list of dictionaries into a well-structured JSON format.'''
        return dumps(list_dictionaries) if list_dictionaries else "[]"

    @staticmethod
    def from_json_string(json_string):
        '''Converts a JSON string back into a list of dictionaries.'''
        return loads(json_string) if json_string else []

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves JSONified objects to a file.'''
        if list_objs is None:
            list_objs = []
        # Convert objects to dictionaries
        list_dict = [obj.to_dictionary() for obj in list_objs]
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_dict))

    @classmethod
    def create(cls, **dictionary):
        '''Creates and loads an instance from a dictionary.'''
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        '''Loads objects from a JSON file and creates instances.'''
        import os
        file_name = f"{cls.__name__}.json"
        if not os.path.isfile(file_name):
            return []
        with open(file_name, "r", encoding="utf-8") as file:
            json_string = file.read()
            dictionaries = cls.from_json_string(json_string)
            return [cls.create(**d) for di in dictionaries]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves objects to a CSV file.'''
        if list_objs is None:
            list_objs = []
    
        data = []
        for obj in list_objs:
            # Check object type and prepare data accordingly
            if isinstance(obj, Rectangle):
                data.append([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif isinstance(obj, Square):
                data.append([obj.id, obj.size, obj.x, obj.y])

        file_name = f"{cls.__name__}.csv"
        with open(file_name, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''Draws shapes using Turtle graphics.'''
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            turtle_pen = turtle.Turtle()
            turtle_pen.color((randrange(255), randrange(255), randrange(255)))
            turtle_pen.pensize(1)
            turtle_pen.penup()
            turtle_pen.pendown()
            turtle_pen.setpos((i.x + turtle_pen.pos()[0], i.y - turtle_pen.pos()[1]))
            turtle_pen.pensize(10)
            turtle_pen.forward(i.width)
            turtle_pen.left(90)
            turtle_pen.forward(i.height)
            turtle_pen.left(90)
            turtle_pen.forward(i.width)
            turtle_pen.left(90)
            turtle_pen.forward(i.height)
            turtle_pen.left(90)
            turtle_pen.end_fill()

        time.sleep(5)
