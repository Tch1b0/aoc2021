def get_input(example: bool = False) -> list[list[str]]:
    """
    Returns the input of the input.txt file
    """
    txt = ""
    with open(f"day_8/{'example_' if example else ''}input.txt", "r") as f:
        txt = f.readlines()
    
    return [[b.split(" ") for b in x.replace("\n","").split(" | ")] for x in txt]

def output(string1: str = "None", string2: str = "None") -> None:
    """
    Write the solution to both parts into the output file
    """
    with open("day_8/output.txt", "w") as f:
        f.write(f"Part 1:\n{string1}\n=========\nPart 2:\n{string2}")

def part1(segments: list[list[str]]) -> int:
    p = 0
    for segment in segments:
        for s in segment[1]:
            if len(s) in [2, 3, 4, 7]:
                p += 1

    return p

def part2() -> str:
    pass

if __name__ == "__main__":
    output(
        part1(get_input()),
        part2()
    )