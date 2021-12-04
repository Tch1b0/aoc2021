def get_input(example: bool = False) -> list[int]:
    """
    Returns the input of the input.txt file
    """
    txt = ""
    with open(f"day_1/{'example_' if example else ''}input.txt", "r") as f:
        txt = f.read()
    
    return [int(x) for x in txt.split()]

def output(string1: str = "None", string2: str = "None") -> None:
    """
    Write the solution to both parts into the output file
    """
    with open("day_1/output.txt", "w") as f:
        f.write(f"Part 1:\n{string1}\n=========\nPart 2:\n{string2}")

def part1(nums: list[int]) -> int:
    recent_depth = 0
    increments = 0
    for depth in nums:
        if depth > recent_depth and recent_depth > 0:
            increments += 1
        recent_depth = depth

    return increments

def part2(nums: list[int]) -> int:
    # Execute the `part1` function with
    # a generated array of summed depths
    return part1([sum(nums[i:i+3]) for i in range(len(nums) - 2)])

if __name__ == "__main__":
    output(
        part1(get_input()), 
        part2(get_input())
    )