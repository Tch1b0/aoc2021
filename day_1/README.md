# Day 1
## Code
```py
def part1(nums: list[int]) -> str:
    recent_depth = 0
    increments = 0
    for depth in nums:
        if depth > recent_depth and recent_depth > 0:
            increments += 1
        recent_depth = depth

    return str(increments)

def part2(nums: list[int]) -> str:
    # Execute the `part1` function with
    # a generated array of summed depths
    return part1([sum(nums[i:i+3]) for i in range(len(nums) - 2)])

```
## Input
```
191
192
201
205
206
203
188
189
...
```
## Output
```
Part 1:
1374
=========
Part 2:
1418
```