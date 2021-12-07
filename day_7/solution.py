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

def most_frequent(submarines):
    costs: list[int] = [0 for _ in range(len(submarines) + 100)]
    for i in range(min(submarines), max(submarines)):
        print(i)
        costs[i] = sum([((x - i) if x > i else (i - x)) for x in submarines])

    return costs.index(min(costs))

def part1(submarines: list[int]) -> str:
    new_pos = most_frequent(submarines)
    print(new_pos)
    fuel_cost = 0
    for submarine_pos in submarines:
        if new_pos > submarine_pos:
            fuel_cost += new_pos - submarine_pos
        elif new_pos < submarine_pos:
            fuel_cost += submarine_pos - new_pos
        elif new_pos == submarine_pos:
            continue
    return fuel_cost

def part2() -> str:
    pass

if __name__ == "__main__":
    output(
        part1(get_input()),
        part2()
    )