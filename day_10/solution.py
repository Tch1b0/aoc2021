from typing import Callable
from colorama import Fore

def get_input(example: bool = False) -> list[str]:
    """
    Returns the input of the input.txt file
    """
    txt = ""
    with open(f"day_10/{'example_' if example else ''}input.txt", "r") as f:
        txt = f.readlines()
    
    return [x.replace("\n", "") for x in txt]

def output(string1: str = "None", string2: str = "None") -> None:
    """
    Write the solution to both parts into the output file
    """
    with open("day_10/output.txt", "w") as f:
        f.write(f"Part 1:\n{string1}\n=========\nPart 2:\n{string2}")

def part1(lines: list[str]) -> int:
    sum_points = 0
    get_points: Callable[[str], int] = lambda s: {"(": 3, ")": 3, "[": 57, "]": 57, "{": 1197, "}": 1197, "<": 25137, ">": 25137}[s]
    get_opening_bracket: Callable[[str], str] = lambda s: {")": "(", "]": "[", "}": "{", ">": "<"}[s]

    for line in lines:
        brackets = []
        for i in range(0, len(line)):
            current_bracket = line[i]
            if current_bracket in ["(", "[", "{", "<"]:
                brackets.append(current_bracket)
            elif current_bracket in [")", "]", "}", ">"]:
                try:
                    brackets.remove(get_opening_bracket(current_bracket))
                except:
                    print(Fore.RED, current_bracket + " ERROR", end="")
                    sum_points += get_points(current_bracket)
                    break
            print(Fore.GREEN, current_bracket, end="")
        else:
            if len(brackets) != 0:
                print(Fore.RED, brackets[-1] + " ERROR", end="")
                sum_points += get_points(brackets[0])

        print()
    
    print(Fore.RESET)
    return sum_points

def part2() -> str:
    pass

if __name__ == "__main__":
    output(
        part1(get_input()),
        part2()
    )