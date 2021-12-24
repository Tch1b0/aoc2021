from __future__ import annotations
from colorama import Fore
from functools import reduce

class Basin():
    def __init__(self, points: list[tuple[int, int]] = []) -> None:
        self.id: int
        self.points = points

    def add_point(self, point: tuple[int, int]) -> None:
        self.points.append(point)

    def has_point(self, point: tuple[int, int]) -> bool:
        return point in self.points

    def move_point(self, other: Basin, point: tuple[int, int]) -> None:
        self.points.remove(point)
        other.add_point(point)

    def size(self) -> int:
        return len(self.points)

    def __gt__(self, other) -> bool:
        return len(self.points) > len(other)
    def __lt__(self, other) -> bool:
        return len(self.points) < len(other)
    def __len__(self):
        return len(self.points)
    def __repr__(self) -> str:
        return str(self.points)

class BasinCollection():
    def __init__(self, basins: list[Basin] = []) -> None:
        self.basins = basins
    
    def add_basin(self, basin: Basin):
        basin.id = len(self.basins)
        self.basins.append(basin)

    def get_basin_by_point(self, point: tuple[int, int]) -> Basin | None:
        if len(basin := [x for x in self.basins if x.has_point(point)]) > 0:
            return basin[0]
        else:
            return None

    def get_basin_by_id(self, id: int) -> Basin | None:
        if len(basin := [x for x in self.basins if x.id == id]) > 0:
            return basin[0]
        else:
            return None

    def sort_basins(self):
        self.basins = sorted(self.basins, key=len, reverse=True)

    def get_top(self, top_count: int) -> list[Basin]:
        self.sort_basins()
        return self.basins[:top_count]

    def get_top_sum(self, top_count: int) -> int:
        return reduce((lambda a,b: a*b), [x.size() for x in self.get_top(top_count)])

def get_input(example: bool = False) -> str:
    """
    Returns the input of the input.txt file
    """
    txt = ""
    with open(f"day_9/{'example_' if example else ''}input.txt", "r") as f:
        txt = f.readlines()
    
    return [[int(g) for g in x.replace("\n", "")] for x in txt]

def output(string1: str = "None", string2: str = "None") -> None:
    """
    Write the solution to both parts into the output file
    """
    with open("day_9/output.txt", "w") as f:
        f.write(f"Part 1:\n{string1}\n=========\nPart 2:\n{string2}")

def get_close_points(points: list[list[tuple[int, int]]], point: tuple[int, int]) -> list[tuple[int, int]]:
    close_points: list[tuple[int, int]] = []
    x, y = point
    current_point_val = points[y][x]

    CURRENT_POINT_RANGE = (current_point_val - 1, current_point_val + 1)
    if y > 0 and points[y - 1][x] != 9 and points[y - 1][x] in CURRENT_POINT_RANGE:
        close_points.append((x, y - 1))
    if x > 0 and points[y][x - 1] != 9 and points[y][x - 1] in CURRENT_POINT_RANGE:
        close_points.append((x - 1, y))
    if x < len(points[y]) - 1 and points[y][x + 1] != 9 and points[y][x + 1] in CURRENT_POINT_RANGE:
        close_points.append((x + 1, y))
    if y < len(points) - 1 and points[y + 1][x] != 9 and points[y + 1][x] in CURRENT_POINT_RANGE:
        close_points.append((x, y + 1))

    return close_points

def smooth(points, basin_collection, visual: bool =True):
    for row in range(0, len(points)):
        row_points: int = 0
        for col in range(0, len(points[row])):
            coords: tuple[int, int] = (col, row)
            current_val: int = points[row][col]
            if current_val == 9:
                if visual: print(Fore.RED, f"{current_val:2d}", end="")
                continue
                
            current_basin: Basin = basin_collection.get_basin_by_point(coords)
            neighbours = get_close_points(points, coords)
            for neighbour in neighbours:
                if current_basin.has_point(neighbour): 
                    continue
                elif (basin := basin_collection.get_basin_by_point(neighbour)).id < current_basin.id:
                    current_basin.move_point(basin, coords)
                    current_basin = basin
            
            for neighbour in neighbours:
                if current_basin.has_point(neighbour): 
                    continue
                else:
                    basin: Basin = basin_collection.get_basin_by_point(neighbour)
                    basin.move_point(current_basin, neighbour)

            if visual: print(Fore.GREEN, f"{current_basin.id:2d}", end="")
        if visual: print()
    if visual: print(Fore.RESET)

def part1(points: list[list[int]], visual: bool = True) -> int:
    risk_levels = 0
    for row in range(0, len(points)):
        for col in range(0, len(points[row])):
            current_point = points[row][col]
            if ((row > 0 and points[row - 1][col] <= current_point) or
                (col > 0 and points[row][col - 1] <= current_point) or
                (col < len(points[row]) - 1 and points[row][col + 1] <= current_point) or
                (row < len(points) - 1 and points[row + 1][col] <= current_point)):
                if visual: print(Fore.RED, current_point, end="")
                continue
            else:
                risk_levels += current_point + 1
                if visual: print(Fore.GREEN, current_point, end="")

        if visual: print()
    if visual: print(Fore.RESET)

    return risk_levels

def part2(points: list[list[int]]) -> int:
    basin_collection: BasinCollection = BasinCollection()
    already_assigned: list[tuple[int, int]] = []

    print()
    for row in range(0, len(points)):
        for col in range(0, len(points[row])):
            coords: tuple[int, int] = (col, row)
            current_val: int = points[row][col]

            if current_val == 9 or coords in already_assigned:
                continue
            
            neighbours = get_close_points(points, coords)
            for neighbour in neighbours:
                if (basin := basin_collection.get_basin_by_point(neighbour)) is not None:
                    basin.add_point(coords)
                    break
            else:
                basin = Basin([coords] + neighbours)
                basin_collection.add_basin(basin)
                already_assigned += neighbours

    print("init for loop", end="\r")
    for i in range(10):
        print(Fore.BLUE, f"Iteration: {i}", end="\r")
        smooth(points, basin_collection, visual=True)
    print(Fore.RESET)
    
    return basin_collection.get_top_sum(3)

if __name__ == "__main__":
    output(
        part1(get_input(), False),
        part2(get_input())
    )