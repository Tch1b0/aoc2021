# Day 2
### [Task](https://adventofcode.com/2021/day/2)
## Code
```py
def part1(commands: list[str]) -> int:
    depth = 0
    h = 0
    for command in commands:
        command = command.split()
        match command[0]:
            case "forward":
                h += int(command[1])
            case "up":
                depth -= int(command[1])
            case "down":
                depth += int(command[1])
    
    return depth * h

def part2(commands: list[str]) -> str:
    depth = 0
    h = 0
    aim = 0
    for command in commands:
        command = command.split()
        match command[0]:
            case "forward":
                h += int(command[1])
                depth += aim * int(command[1])
            case "up":
                aim -= int(command[1])
            case "down":
                aim += int(command[1])
    
    return depth * h

```
## Input
```
forward 9
down 9
up 4
down 5
down 6
up 6
down 7
down 1
...
```
## Output
```
Part 1:
1499229
=========
Part 2:
1340836560
```