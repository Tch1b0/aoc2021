from typing import Any


def get_input(example: bool = False) -> str:
    """
    Returns the input of the input.txt file
    """
    txt = ""
    with open(f"day_14/{'example_' if example else ''}input.txt", "r") as f:
        txt = [x.replace("\n", "") for x in f.readlines() if x != "\n"]

    base = txt[0]
    rules = {}
    for i, val in enumerate(txt):
        if i == 0:
            continue
        tmp = val.replace(" ", "").split("->")
        rules[tmp[0]] = tmp[1]

    return {
        "base": base,
        "rules": rules
    }


def output(string1: str = "None", string2: str = "None") -> None:
    """
    Write the solution to both parts into the output file
    """
    with open("day_14/output.txt", "w") as f:
        f.write(f"Part 1:\n{string1}\n=========\nPart 2:\n{string2}")


def part1(inp: dict[str, Any]) -> int:
    rules: dict[str, str] = inp["rules"]

    polymer: str = inp["base"]
    for _ in range(10):
        new_pol = ""
        for i in range(0, len(polymer) - 1):
            pair = polymer[i:i+2]
            new_pol += pair[0] + rules[pair]

        polymer = new_pol + polymer[-1]

    char_occurences = {}
    for char in set(polymer):
        char_occurences[char] = polymer.count(char)

    tmp = sorted(char_occurences.values())

    return tmp[-1] - tmp[0]


def part2() -> str:
    pass


if __name__ == "__main__":
    output(
        part1(get_input()),
        part2()
    )
