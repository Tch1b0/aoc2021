from colorama import Fore

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

def part1(points: list[list[int]]) -> int:
    risk_levels = 0
    for row in range(0, len(points)):
        for col in range(0, len(points[row])):
            current_point = points[row][col]
            if ((row > 0 and points[row - 1][col] <= current_point) or
                (col > 0 and points[row][col - 1] <= current_point) or
                (col < len(points[row]) - 1 and points[row][col + 1] <= current_point) or
                (row < len(points) - 1 and points[row + 1][col] <= current_point)):
                print(Fore.RED, current_point, end="")
                continue
            else:
                risk_levels += current_point + 1
                print(Fore.GREEN, current_point, end="")

        print()
    print(Fore.RESET)

    return risk_levels

def find_and_append(basins: list[list[tuple[int, int]]], seach_val: tuple[int, int], append_val: tuple[int, int]) -> list[list[tuple[int, int]]]:
    for basin in basins:
        if seach_val in basin: 
            basin.append(append_val)
            break
    else:
        basins.append([append_val])
    
    return basins

def part2(points: list[list[int]]) -> int:
    basins: list[list[tuple[int, int]]] = []
    for row in range(0, len(points)):
        for col in range(0, len(points[row])):
            current_point = points[row][col]
            if current_point == 9:
                print(Fore.RED, current_point, end="")
                continue

            search_val: tuple
            CURRENT_POINT_RANGE = [current_point - 1, current_point + 1]
            if row > 0 and points[row - 1][col] in CURRENT_POINT_RANGE:
                search_val = (col, row - 1)
            elif col > 0 and points[row][col - 1] in CURRENT_POINT_RANGE:
                search_val = (col - 1, row)
            elif col < len(points[row]) - 1 and points[row][col + 1] in CURRENT_POINT_RANGE:
                search_val = (col + 1, row)
            elif row < len(points) - 1 and points[row + 1][col] in CURRENT_POINT_RANGE:
                search_val = (col, row + 1)
            else:
                print(Fore.RED, current_point, end="")

            find_and_append(basins, search_val, (col, row))
            print(Fore.GREEN, current_point, end="")
        print()

    print(Fore.RESET)
    print(basins)

    result = 1
    for _ in range(3):
        tmp = max(basins, key=len)
        result *= len(tmp)
        basins.remove(tmp)

    return result
    


if __name__ == "__main__":
    output(
        part1(get_input()),
        part2()
    )