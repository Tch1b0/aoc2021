from typing import Any


def get_input(example: bool = False) -> str:
    """
    Returns the input of the input.txt file
    """

    content = {
        "points": [],
        "instructions": []
    }
    with open(f"day_13/{'example_' if example else ''}input.txt", "r") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            if line in [" ", ""]:
                continue
            elif line.startswith("fold"):
                content["instructions"].append(
                    line.replace("fold along ", "").split("="))
            else:
                coord = Coordinates(*[int(x) for x in line.split(",")])
                content["points"].append(coord)

    return content


def output(string1: str = "None", string2: str = "None") -> None:
    """
    Write the solution to both parts into the output file
    """
    with open("day_13/output.txt", "w") as f:
        f.write(f"Part 1:\n{string1}\n=========\nPart 2:\n{string2}")


class Coordinates():
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other):
        if type(other) is Coordinates:
            return self.x == other.x and self.y == other.y
        else:
            raise ValueError()


class Paper():
    points: list[Coordinates] = []

    def __init__(self, points: list[Coordinates] | list[tuple[int, int]] = None) -> None:
        if points:
            for point in points:
                self.add_point(point)

    def add_point(self, coords: Coordinates | tuple[int, int]) -> None:
        if type(coords) is tuple:
            coords = Coordinates(*coords)

        self.points.append(coords)

    def fold(self, axis: str, ordinate: int):
        if axis == "y":
            for point in self.points:
                if point.y > ordinate:
                    diff = point.y - ordinate
                    point.y -= diff*2 - (1 if diff != 1 else 0)
        else:
            for point in self.points:
                if point.x > ordinate:
                    diff = point.x - ordinate
                    point.x -= diff*2 - (1 if diff != 1 else 0)


def part1(inp: dict[str, Any]) -> int:
    paper = Paper(inp["points"])
    for axis, ordinate in inp["instructions"]:
        paper.fold(axis, int(ordinate))

    return len(set(paper.points))


def part2(_) -> str:
    pass


if __name__ == "__main__":
    output(
        part1(get_input()),
        part2(get_input())
    )
