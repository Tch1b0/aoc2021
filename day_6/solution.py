def get_input(example: bool = False) -> list[int]:
    """
    Returns the input of the input.txt file
    """
    txt = ""
    with open(f"day_6/{'example_' if example else ''}input.txt", "r") as f:
        txt = f.read()
    
    return [int(x) for x in txt.split(",")]

def output(string1: str = "None", string2: str = "None") -> None:
    """
    Write the solution to both parts into the output file
    """
    with open("day_6/output.txt", "w") as f:
        f.write(f"Part 1:\n{string1}\n=========\nPart 2:\n{string2}")

def part1(inp) -> int:
    return count_fishes(inp, 80)

def count_fishes(initial_fishes: list[int], days: int):
    day = 6
    week = 0
    fishes = [initial_fishes.count(x) for x in range(0, 6 + 1)]
    week_fishes: dict[int, list[int]] = {}
    for _ in range(days):
        new_fish_day = day + (-2) if day > 1 else 5 + day
        if week + 1 in week_fishes.keys():
            week_fishes[week + 1][new_fish_day] += fishes[day]
        else:
            week_fishes[week + 1] = [0, 0, 0, 0, 0, 0, 0]
        if day == 0:
            week += 1
            day = 6
            tmp = [fishes[5], fishes[6]]
            fishes = [week_fishes[week][i] + fishes[i] for i in range(0, 4 + 1)]
            fishes.append(tmp[0])
            fishes.append(tmp[1])
            if week != 1:
                fishes[5] += week_fishes[week - 1][5]
                fishes[6] += week_fishes[week - 1][6]
                
        else:
            day -= 1

    return sum(fishes) + sum(week_fishes[week])

def part2(inp) -> str:
    count_fishes(inp, 256)

if __name__ == "__main__":
    output(
        part1(),
        part2()
    )