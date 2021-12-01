# returns the puzzle input
def get_input() -> str:
    txt = ""
    with open("{{ROOT}}/input.txt", "r") as f:
        txt = f.read()
    
    return txt

# write the solution to the output file
def output(string1: str = "None", string2: str = "None") -> None:
    with open("{{ROOT}}/output.txt", "w") as f:
        f.write(f"Part 1:\n{string1}\n=========\nPart 2:\n{string2}")

def part1():
    pass

def part2():
    pass

if __name__ == "__main__":
    output(
        part1(),
        part2()
    )