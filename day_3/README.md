# Day 3
#### [Task](https://adventofcode.com/2021/day/3)
## Code
```py
def part1(bits: list[str]) -> str:
    gamma_rate = ""
    for i in range(0, len(bits[0])):
        bit_parts = [bit[i] for bit in bits]
        if bit_parts.count("1") > bit_parts.count("0"):
            gamma_rate += "1"
        else:
            gamma_rate += "0"
    return int(gamma_rate, 2) * int(gamma_rate.replace("1","!").replace("0","1").replace("!","0"), 2)

def part2(all_bits: list[str]) -> str:
    bits = all_bits.copy()

    for i in range(0, len(bits[0])):
        if len(bits) == 1:
            break
        bit_parts = [bit[i] for bit in bits]
        if bit_parts.count("1") >= bit_parts.count("0"):
            bits = [bit for bit in bits if bit[i] == "1"]
        else:
            bits = [bit for bit in bits if bit[i] == "0"]
    
    oxygen = bits[0]
    bits = all_bits.copy()

    for i in range(0, len(bits[0])):
        if len(bits) == 1:
            break
        bit_parts = [bit[i] for bit in bits]
        if bit_parts.count("1") >= bit_parts.count("0"):
            bits = [bit for bit in bits if bit[i] == "0"]
        else:
            bits = [bit for bit in bits if bit[i] == "1"]

    co2 = bits[0]

    return int(oxygen, 2) * int(co2, 2)

```
## Input
```
101000001100
011111100111
111100001110
110000011001
001001001011
010011101000
011001110011
010100010000
...
```
## Output
```
Part 1:
1092896
=========
Part 2:
4672151
```