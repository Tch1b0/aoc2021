def get_input() -> str:
    """
    Returns the input of the input.txt file
    """
    txt = ""
    with open("day_3/input.txt", "r") as f:
        txt = f.read()
    
    return txt.split()

def output(string1: str = "None", string2: str = "None") -> None:
    """
    Write the solution to both parts into the output file
    """
    with open("day_3/output.txt", "w") as f:
        f.write(f"Part 1:\n{string1}\n=========\nPart 2:\n{string2}")

def part1(bits: list[str]) -> str:
    gamma_rate = ""
    for i in range(0, len(bits[0])):
        current_bit = [bit[i] for bit in bits]
        if current_bit.count("1") > current_bit.count("0"):
            gamma_rate += "1"
        else:
            gamma_rate += "0"
    return int(gamma_rate, 2) * int(gamma_rate.replace("1","!").replace("0","1").replace("!","0"), 2)

def part2() -> str:
    pass

if __name__ == "__main__":
    output(
        part1(get_input()),
        part2()
    )