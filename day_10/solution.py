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


bracket_pairs = {
    ")": "(", "]": "[", "}": "{", ">": "<"}

get_opening_bracket: Callable[[str], str] = lambda s: bracket_pairs[s]
get_closing_brackets: Callable[[str], str] = lambda s: {
    x[1]: x[0] for x in bracket_pairs.items()}[s]


def part1(lines: list[str]) -> int:
    score = 0
    get_points: Callable[[str], int] = lambda s: {
        "(": 3, ")": 3, "[": 57, "]": 57, "{": 1197, "}": 1197, "<": 25137, ">": 25137}[s]

    for line in lines:
        brackets = []
        for bracket in line:
            try:
                opening = get_opening_bracket(bracket)
                if len(bracket) == 0 or brackets[-1] != opening:
                    score += get_points(bracket)
                    print(Fore.RED, bracket, "ERROR", end="")
                    break
                else:
                    brackets.pop()
            except KeyError:
                print(Fore.GREEN, bracket, end="")
                brackets.append(bracket)
        print()

    print(Fore.RESET)
    return score


def part2(lines: list[str]) -> int:
    def get_points(s): return {")": 1, "]": 2, "}": 3, ">": 4}[s]

    # Remove invalid lines
    for line in lines.copy():
        brackets = []
        for bracket in line:
            if bracket in bracket_pairs.values():
                brackets.append(bracket)
            elif bracket != get_closing_brackets(brackets[-1]):
                lines.remove(line)
                break
            else:
                brackets.pop()

    scores = []

    # Fill in missing brackets
    for line in lines:
        loc_score = 0
        ignored = []
        print(Fore.BLUE, line, end="")
        for bracket in line[::-1]:
            if bracket in bracket_pairs.keys():
                ignored.append(get_opening_bracket(bracket))
            elif bracket in ignored:
                ignored.remove(bracket)
            else:
                closing_bracket = get_closing_brackets(bracket)
                print(Fore.GREEN, closing_bracket, end="")
                loc_score *= 5
                loc_score += get_points(closing_bracket)
        scores.append(loc_score)
        print()

    print(Fore.RESET)

    return sorted(scores)[int(len(scores)/2)]


if __name__ == "__main__":
    inp = get_input()
    output(
        part1(inp.copy()),
        part2(inp.copy())
    )
