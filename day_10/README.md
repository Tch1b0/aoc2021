# Day 10

### [Task](https://adventofcode.com/2021/day/10)

## Code

```py
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


```

## Input

```
<[<<({{<{<[[([()][()()])<{[]<>}{<>}>><<<[]{}>>{<<><>>({}{})}>][<<<{}<>>([])>{<{}><()>}>]><(<{(()[]){[](
<{([({{[(<[({({}{})[()<>]}{{<>{}}[(){}]})]>({(<<<><>>{{}()}>)<<<[]><{}<>>><[{}[]]<<>[]>>>}))[{(<{([]
([<([({(<([<({()()}(<>[]))[<[]()>{<>{}}]>]<{{{{}{}}{()()})({[]}[<>{}])}>)>)}){<<{{(<<<()<>><<><>>>
[{{[<<[{([[{{[<>{}]<()<>>}[(()<>)[{}<>]]}<<[{}[]]([]<>)>{{[]{}}{()()}}>]][[{<({}{})<[]{}>>
<<{{<([(((([{<[]<>>{()<>}}(<<>[]>{(){}})]([{{}<>}<[]>](<[][]><{}()>)))))[({{{<[]{}>[()]}<<<><>>
<(<[{(<[{{{<{[[]<>]{<>()}}><[[{}()][(){}]]>}}<[<[<()()>({}<>)]><[{[]()}([][])](<(){}>[<><>])>]{
{[[<{{<<[[<<(({}<>){<><>})[[<>()][[]{})]>[[[{}[]]<<>>]{(<>[])}]>{{<<()[]>{<>{}}>[{[]<>}<[]{}>]
({[((((([{[({[{}[]]<[]()>}[({}{})<<>[]>])<[(()[])<{}()>]{[[]<>]{[]()})>](([({}<>)(()[])][<[]{}>])
...
```

## Output

```
Part 1:
216297
=========
Part 2:
2165057169
```
