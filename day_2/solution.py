def get_input(example: bool = False) -> str:
    """
    Returns the input of the input.txt file
    """
    txt = ""
    with open(f"day_2/{'example_' if example else ''}input.txt", "r") as f:
        txt = f.read()
    
    return txt.split("\n")

def output(string1: str = "None", string2: str = "None") -> None:
    """
    Write the solution to both parts into the output file
    """
    with open("day_2/output.txt", "w") as f:
        f.write(f"Part 1:\n{string1}\n=========\nPart 2:\n{string2}")

def part1(commands: list[str]) -> int:
    depth = 0
    h = 0
    for command in commands:
        command = command.split()
        match command[0]:
            case "forward":
                h += int(command[1])
            case "up":
                depth -= int(command[1])
            case "down":
                depth += int(command[1])
    
    return depth * h

def part2(commands: list[str]) -> int:
    depth = 0
    h = 0
    aim = 0
    for command in commands:
        command = command.split()
        match command[0]:
            case "forward":
                h += int(command[1])
                depth += aim * int(command[1])
            case "up":
                aim -= int(command[1])
            case "down":
                aim += int(command[1])
    
    return depth * h

if __name__ == "__main__":
    output(
        part1(get_input()),
        part2(get_input())
    )