# Day 14
### [Task](https://adventofcode.com/2021/day/14)
## Code
```py
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


```
## Input
```
CFFPOHBCVVNPHCNBKVNV

KO -> F
CV -> H
CF -> P
FK -> B
BN -> P
VN -> K
...
```
## Output
```
Part 1:
2947
=========
Part 2:
None
```