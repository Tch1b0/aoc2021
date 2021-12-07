from typing import Callable


def get_input(example: bool = False) -> str:
    """
    Returns the input of the input.txt file
    """
    txt = ""
    with open(f"day_7/{'example_' if example else ''}input.txt", "r") as f:
        txt = f.read()
    
    return [int(x) for x in txt.split(",")]

def output(string1: str = "None", string2: str = "None") -> None:
    """
    Write the solution to both parts into the output file
    """
    with open("day_7/output.txt", "w") as f:
        f.write(f"Part 1:\n{string1}\n=========\nPart 2:\n{string2}")

def most_efficient_ordinate(submarines: list[int], complex: bool = False):
    costs: list[int] = [0 for _ in range(0, (max(submarines) - min(submarines)))]
    get_fuel_cost: Callable[[int, int], int]
    if not complex:
        get_fuel_cost = lambda p1, p2: (p1 - p2) if p1 > p2 else (p2 - p1)
    else:
        get_fuel_cost = complex_fuel_cost

    for i in range(min(submarines), max(submarines)):
        costs[i] = sum([get_fuel_cost(x, i) for x in submarines])

    return min(costs)

def complex_fuel_cost(point1: int, point2: int):
    start, end = (point1, point2) if point1 < point2 else (point2, point1)
    fuel_increment = 1
    fuel_cost = 0
    for _ in range(start, end):
        fuel_cost += fuel_increment
        fuel_increment += 1
    
    return fuel_cost

def part1(submarines: list[int]) -> str:
    return most_efficient_ordinate(submarines)

def part2(submarines: list[int]) -> str:
    return most_efficient_ordinate(submarines, complex=True)


if __name__ == "__main__":
    output(
        part1(get_input()),
        part2(get_input())
    )