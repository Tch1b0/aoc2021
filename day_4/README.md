# Day 4
### [Task](https://adventofcode.com/2021/day/4)
## Code
```py
def part1(bingo_numbers: list[str], bingo_fields: list[BingoField]) -> int:
    for num in bingo_numbers:
        for field in bingo_fields:
            field.mark_number(num)
            if field.has_won():
                return sum(field.get_unmarked_numbers_as_int()) * int(num)


def part2(bingo_numbers: list[str], bingo_fields: list[BingoField]) -> int:
    last_field_sum_won: int
    last_num_won: int
    bingoed: list[BingoField] = []

    for num in bingo_numbers:
        for field in bingo_fields:
            if field in bingoed: continue
            field.mark_number(num)
            if field.has_won():
                bingoed.append(field)
                last_field_sum_won = sum(field.get_unmarked_numbers_as_int())
                last_num_won = int(num)


        if len(bingo_fields) == 0:
            break

    return last_field_sum_won * last_num_won

```
## Input
```
62,55,98,93,48,28,82,78,19,96,31,42,76,25,34,4,18,80,66,6,14,17,57,54,90,27,40,47,9,36,97,56,87,61,91,1,64,71,99,38,70,5,94,85,49,59,69,26,21,60,0,79,2,95,11,84,20,24,8,51,46,44,88,22,16,53,7,32,89,67,15,86,41,92,10,77,68,63,43,75,33,30,81,37,83,3,39,65,12,45,23,73,72,29,52,58,35,50,13,74

10 83 98 12 33
38 68  2 99 85
16 89 54 50 97
31  8 17 11 76
 0 55 66 32 87

...
```
## Output
```
Part 1:
12796
=========
Part 2:
18063
```