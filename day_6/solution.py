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

def part1(fishes: list[int]) -> int:
    for _ in range(80):
        append_me = []
        for i in range(0, len(fishes)):
            if fishes[i] == 0:
                fishes[i] = 6
                append_me.append(8)
            else:
                fishes[i] -= 1
        fishes += append_me

    return len(fishes)

def part2(initial_fishes: list[int]):
    fishes = [initial_fishes.count(x) for x in range(0, 8 + 1)]
    for _ in range(256):
        tomorrow_fishes = [0, 0, 0 ,0 ,0, 0, 0, 0, 0]
        tmp = fishes[0]
        for i in range(9):
            tomorrow_fishes[i - 1] = fishes[i]

        tomorrow_fishes[6] += tmp
        tomorrow_fishes[8] = tmp
        fishes = tomorrow_fishes
    
    return sum(fishes)

if __name__ == "__main__":
    output(
        part1(get_input()),
        part2(get_input())
    )