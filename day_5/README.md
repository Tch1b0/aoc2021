# Day 5
### [Task](https://adventofcode.com/2021/day/5)
## Code
```py
def part1(game_field: GameField) -> int:
    return game_field.count_overlapping_vents(diagonal=False)

def part2(game_field: GameField) -> int:
    return game_field.count_overlapping_vents(diagonal=True)

```
## Input
```
541,808 -> 108,808
982,23 -> 45,960
558,21 -> 558,318
907,877 -> 43,13
532,213 -> 532,801
599,387 -> 870,387
762,208 -> 78,208
739,527 -> 739,907
...
```
## Output
```
Part 1:
7674
=========
Part 2:
20898
```