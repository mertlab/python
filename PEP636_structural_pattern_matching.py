
import json
from dataclasses import dataclass
from enum import Enum

class PatternMatchingGame:

    def __init__(self):
        self._characters = list("Joe")
        self._rooms = dict({"room1": {"up": "room2", "down": "room3"}, "room2": {"down": "room1"}, "room3": {"up": "room1"}})
        self._current_character = "Joe"
        self._current_room = "room1"
        self._current_items = list()

    def quit_game(self):
        exit()

    def look_around(self):
        pass

    # [action, obj] = command.split()
    def set_command(self, command):
        match command.split():
            case ["quit"]:
                print("Goodbye!")
                self.quit_game()
            case ["look"]:
                self.look_around()
            case ["get", obj] | ["pick", obj, "up"] | ["pick", "up", obj]:
                self._current_items.append(obj)
                print(f"Current Items: {self._current_items}")
            case ["go", direction] if direction in self._rooms[self._current_room].keys():
                print(f"Direction: {direction}")
                self._current_room = self._rooms[self._current_room][direction]
                print(f"Current Room: {self._current_room}")
            case ["go", _]:
                print(f"Cannot go that way")
            case ["drop", *items]:
                {self._current_items.remove(item) for item in items}
                print(f"Remaining items: {self._current_items}")
            case _:
                print(f"Sorry, I couldn't understand {command!r}")

    def set_command_map(self, command_map):
        match command_map:
            case {"text": str(message), "color": str(c)}:
                print(f"Text message: {message}, color: {c}")
            case {"sleep": float(duration)}:
                print(f"Sleeping {duration}")
            case {"sound": str(url), "format": "ogg" as format}:
                print(f"Sound format: {format} in {url}")
            case {"sound": _, "format": _}:
                print("Unsupported format")

@dataclass
class Point:
    x: int
    y: int

class PointFinder:
    def where_is(point):
        match point:
            case Point(x=0, y=0):
                print("Origin")
            case Point(x=0, y=y):
                print(f"y: {y}")
            case Point(x=x, y=0):
                print(f"x: {x}")
            case Point(x, y) if x == y:
                print(f"Y=X at {x}")
            case Point(x, y):
                print(f"Not on the diagonal")
            case _:
                print("Not a point")

class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2

    def show(self):
        match self:
            case Color.RED:
                print("I see red!")
            case Color.GREEN:
                print("Grass is green")
            case Color.BLUE:
                print("Sky is blue")


def __main__():
    game = PatternMatchingGame()
    point_finder = PointFinder()

    point_finder.where_is(Point(1,0))
    point_finder.where_is(Point(1,1))
    point_finder.where_is(Point(1,2))
    point_finder.where_is(game)

    color = Color.GREEN
    color.show()

    while(1):
        command = input("What are we doing next? ")
        game.set_command(command)
        command_map = input("Command Map? ")
        game.set_command_map(command_map=json.loads(command_map))

__main__()
