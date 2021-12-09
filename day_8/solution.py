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

def bcd_to_int(
    code: str, 
    rel: dict[str, str] = {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g"}
    ) -> int:
    segments = [rel[char] for char in code]
    number_codes: list[list[str]] = [
        ["a", "b", "c", "e", "f", "g"],
        ["c", "f"],
        ["a", "c", "d", "e", "g"],
        ["a", "c", "d", "f", "g"],
        ["b", "c", "d", "f"],
        ["a", "b", "d", "f", "g"],
        ["a", "b", "d", "e", "f", "g"],
        ["a", "c", "f"],
        ["a", "b", "c", "d", "e", "f", "g"],
        ["a", "b", "c", "d", "f", "g"]
    ]
    return number_codes.index(segments)

def decrypt_segment(segment: list[str]):
    pass 

def part1(segments: list[list[str]]) -> int:
    p = 0
    for segment in segments:
        for s in segment[1]:
            if len(s) in [2, 3, 4, 7]:
                p += 1

    return p

def part2(segments) -> str:
    for segment in segments:
        decrypt_segment(segment)

if __name__ == "__main__":
    output(
        part1(get_input()),
        part2(get_input())
    )