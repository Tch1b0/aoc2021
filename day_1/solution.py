def get_input() -> list[int]:
    """
    Returns the input of the input.txt file
    """
    txt = ""
    with open("day_1/input.txt", "r") as f:
        txt = f.read()
    
    return [int(x) for x in txt.split()]

def output(string1: str, string2: str = "None") -> None:
    """
    Write the solution to both parts into the output file
    """
    with open("day_1/output.txt", "w") as f:
        f.write(f"Part 1:\n{string1}\n=========\nPart 2:\n{string2}")

def part1(nums: list[int]) -> str:
    recent_depth = 0
    increments = 0
    for depth in nums:
        if depth > recent_depth and recent_depth > 0:
            increments += 1
        recent_depth = depth
    
    return str(increments)

def part2(nums: list[int]) -> str:
    new_nums: list[int] = []
    for i in range(0, len(nums) - 2):
        new_nums.append(nums[i] + nums[i+1] + nums[i+2])

    return part1(new_nums)

if __name__ == "__main__":
    output(
        part1(get_input()), 
        part2(get_input())
    )