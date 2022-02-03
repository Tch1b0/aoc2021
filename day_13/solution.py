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
                coord = Coordinate(*[int(x) for x in line.split(",")])
                content["points"].append(coord)

    return content


def output(string1: str = "None", string2: str = "None") -> None:
    """
    Write the solution to both parts into the output file
    """
    with open("day_13/output.txt", "w") as f:
        f.write(f"Part 1:\n{string1}\n=========\nPart 2:\n{string2}")


class Coordinate():
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
        if type(other) is Coordinate:
            return self.x == other.x and self.y == other.y
        else:
            raise ValueError()


class Paper():
    points: list[Coordinate] = []

    def __init__(self, points: list[Coordinate] | list[tuple[int, int]] = None) -> None:
        if points:
            for point in points:
                self.add_point(point)

    def contains_point(self, coords: Coordinate | tuple[int, int]) -> bool:
        if type(coords) is not Coordinate:
            coords = Coordinate(*coords)

        return coords in self.points

    def add_point(self, coords: Coordinate | tuple[int, int]) -> None:
        if type(coords) is tuple:
            coords = Coordinate(*coords)

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


def part1(inp: dict[str, Any], verbose: bool = True) -> int:
    paper = Paper(inp["points"])
    for axis, ordinate in inp["instructions"]:
        if verbose:
            max_x = sorted(paper.points, key=lambda x: x.x)[-1].x
            max_y = sorted(paper.points, key=lambda x: x.y)[-1].y
            for i in range(max_y):
                for j in range(max_x):
                    print("#" if paper.contains_point((j, i)) else ".", end="")
                print()
            print()
        paper.fold(axis, int(ordinate))

    return len(set(paper.points))

def part2(_) -> None:
    pass


if __name__ == "__main__":
    output(
        part1(get_input(), False),
        part2(get_input())
    )
