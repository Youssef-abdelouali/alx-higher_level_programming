#!/usr/bin/python3

'''Module for Base class.'''

import json
import csv
import turtle
from typing import List, Dict, Any, Union


class Base:
    __nb_objects = 0

    def __init__(self, id: Union[int, None] = None) -> None:
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries: List[Dict[str, Any]]) -> str:
        """Converts a list of dictionaries to a JSON string."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs: List[Any]) -> None:
        """Saves a list of objects to a JSON file."""
        file_name = f"{cls.__name__}.json"
        try:
            with open(file_name, "w") as json_file:
                if list_objs is None:
                    json_file.write("[]")
                else:
                    list_dicts = [o.to_dictionary() for o in list_objs]
                    json_file.write(Base.to_json_string(list_dicts))
        except IOError as e:
            print(f"Error saving to file: {e}")

    @staticmethod
    def from_json_string(json_string: str) -> List[Dict[str, Any]]:
        """Converts a JSON string to a list of dictionaries."""
        if not json_string or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary: Any) -> Any:
        """Creates an object from a dictionary."""
        if dictionary:
            new = cls(1) if cls.__name__ == "Rectangle" else cls(1, 1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls) -> List[Any]:
        """Loads objects from a JSON file."""
        file_name = f"{cls.__name__}.json"
        try:
            with open(file_name, "r") as json_file:
                list_dicts = Base.from_json_string(json_file.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs: List[Any]) -> None:
        """Saves a list of objects to a CSV file."""
        file_name = f"{cls.__name__}.csv"
        try:
            with open(file_name, "w", newline="") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=cls.fieldnames())
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
        except IOError as e:
            print(f"Error saving to CSV file: {e}")

    @classmethod
    def load_from_file_csv(cls) -> List[Any]:
        """Loads objects from a CSV file."""
        file_name = f"{cls.__name__}.csv"
        try:
            with open(file_name, "r", newline="") as csv_file:
                reader = csv.DictReader(csv_file)
                list_dicts = [dict((a, int(b)) for a, b in d.items()) for d in reader]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles: List[Any], list_squares: List[Any]) -> None:
        """Draws rectangles and squares using turtle."""
        draw_turtle = turtle.Turtle()
        draw_turtle.screen.bgcolor("#b7312c")
        draw_turtle.pensize(3)
        draw_turtle.shape("turtle")

        Base.draw_objects(draw_turtle, "#ffffff", list_rectangles)
        Base.draw_objects(draw_turtle, "#b5e3d8", list_squares)

        turtle.exitonclick()

    @staticmethod
    def draw_objects(draw_turtle: turtle.Turtle, color: str, objects: List[Any]) -> None:
        """Draws objects using turtle."""
        draw_turtle.color(color)
        for obj in objects:
            draw_turtle.showturtle()
            draw_turtle.up()
            draw_turtle.goto(obj.x, obj.y)
            draw_turtle.down()
            for _ in range(2):
                draw_turtle.forward(obj.width)
                draw_turtle.left(90)
                draw_turtle.forward(obj.height)
                draw_turtle.left(90)
            draw_turtle.hideturtle()

    @classmethod
    def fieldnames(cls) -> List[str]:
        """Returns fieldnames for CSV files."""
        return ["id", "width", "height", "x", "y"] if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]
