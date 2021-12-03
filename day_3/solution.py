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

def part1(bits: list[str]) -> int:
    gamma_rate = ""
    for i in range(0, len(bits[0])):
        bit_parts = [bit[i] for bit in bits]
        if bit_parts.count("1") > bit_parts.count("0"):
            gamma_rate += "1"
        else:
            gamma_rate += "0"
    return int(gamma_rate, 2) * int(gamma_rate.replace("1","!").replace("0","1").replace("!","0"), 2)

def part2(all_bits: list[str]) -> int:
    bits = all_bits.copy()

    for i in range(0, len(bits[0])):
        if len(bits) == 1:
            break
        bit_parts = [bit[i] for bit in bits]
        if bit_parts.count("1") >= bit_parts.count("0"):
            bits = [bit for bit in bits if bit[i] == "1"]
        else:
            bits = [bit for bit in bits if bit[i] == "0"]
    
    oxygen = bits[0]
    bits = all_bits.copy()

    for i in range(0, len(bits[0])):
        if len(bits) == 1:
            break
        bit_parts = [bit[i] for bit in bits]
        if bit_parts.count("1") >= bit_parts.count("0"):
            bits = [bit for bit in bits if bit[i] == "0"]
        else:
            bits = [bit for bit in bits if bit[i] == "1"]

    co2 = bits[0]

    return int(oxygen, 2) * int(co2, 2)

if __name__ == "__main__":
    i = get_input()
    output(
        part1(i),
        part2(i)
    )