# Day 6
### [Task](https://adventofcode.com/2021/day/6)
## Code
```py
def part1(fishes: list[int]) -> int:
    for _ in range(80):
        append_me = []
        for i in range(0, len(fishes)):
            if fishes[i] == 0:
                fishes[i] = 6
                append_me.append(8)
            else:
                fishes[i] -= 1
        fishes += append_me

    return len(fishes)

def part2(initial_fishes: list[int]):
    fishes = [initial_fishes.count(x) for x in range(0, 8 + 1)]
    for _ in range(256):
        tomorrow_fishes = [0, 0, 0 ,0 ,0, 0, 0, 0, 0]
        tmp = fishes[0]
        for i in range(9):
            tomorrow_fishes[i - 1] = fishes[i]

        tomorrow_fishes[6] += tmp
        tomorrow_fishes[8] = tmp
        fishes = tomorrow_fishes
    
    return sum(fishes)

```
## Input
```
3,4,1,1,5,1,3,1,1,3,5,1,1,5,3,2,4,2,2,2,1,1,1,1,5,1,1,1,1,1,3,1,1,5,4,1,1,1,4,1,1,1,1,2,3,2,5,1,5,1,2,1,1,1,4,1,1,1,1,3,1,1,3,1,1,1,1,1,1,2,3,4,2,1,3,1,1,2,1,1,2,1,5,2,1,1,1,1,1,1,4,1,1,1,1,5,1,4,1,1,1,3,3,1,3,1,3,1,4,1,1,1,1,1,4,5,1,1,3,2,2,5,5,4,3,1,2,1,1,1,4,1,3,4,1,1,1,1,2,1,1,3,2,1,1,1,1,1,4,1,1,1,4,4,5,2,1,1,1,1,1,2,4,2,1,1,1,2,1,1,2,1,5,1,5,2,5,5,1,1,3,1,4,1,1,1,1,1,1,1,4,1,1,4,1,1,1,1,1,2,1,2,1,1,1,5,1,1,3,5,1,1,5,5,3,5,3,4,1,1,1,3,1,1,3,1,1,1,1,1,1,5,1,3,1,5,1,1,4,1,3,1,1,1,2,1,1,1,2,1,5,1,1,1,1,4,1,3,2,3,4,1,3,5,3,4,1,4,4,4,1,3,2,4,1,4,1,1,2,1,3,1,5,5,1,5,1,1,1,5,2,1,2,3,1,4,3,3,4,3
```
## Output
```
Part 1:
379414
=========
Part 2:
1705008653296
```