def get_input(example: bool = False) -> str:
    """
    Returns the input of the input.txt file
    """
    txt = ""
    with open(f"day_24/{'example_' if example else ''}input.txt", "r") as f:
        txt = f.read()
    
    return txt

def output(string1: str = "None", string2: str = "None") -> None:
    """
    Write the solution to both parts into the output file
    """
    with open("day_24/output.txt", "w") as f:
        f.write(f"Part 1:\n{string1}\n=========\nPart 2:\n{string2}")

class ALU():
    def __init__(self, code: str) -> None:
        self.code: list = [[b for b in x.split(" ")] for x in code.split("\n") if x != ""]
        self.reset()
    
    def run(self, inp: str = None) -> None:
        v = self.variables
        inp_index = 0
        for tmp in self.code:
            if len(tmp) == 2:
                operation, l_operand = tmp
            else:
                operation, l_operand, r_operand = tmp
            match operation:
                case "inp":
                    v[l_operand] = int(inp[inp_index])
                    inp_index += 1
                case "add":
                    # print(f"Adding {self.var_or_num(r_operand)} to {l_operand}(={v[l_operand]})")
                    v[l_operand] = v[l_operand] + self.var_or_num(r_operand)
                case "mul":
                    # print(f"Multiplying {self.var_or_num(r_operand)} to {l_operand}(={v[l_operand]})")
                    v[l_operand] = v[l_operand] * self.var_or_num(r_operand)
                case "div":
                    # print(f"Dividing {self.var_or_num(r_operand)} from {l_operand}(={v[l_operand]})")
                    v[l_operand] = int(v[l_operand] / self.var_or_num(r_operand))
                case "mod":
                    # print(f"Modulate {self.var_or_num(r_operand)} from {l_operand}(={v[l_operand]})")
                    v[l_operand] = v[l_operand] % self.var_or_num(r_operand)
                case "eql":
                    # print(f"Decide wether {l_operand}(={v[l_operand]}) equals {self.var_or_num(r_operand)}")
                    v[l_operand] = int(v[l_operand] == self.var_or_num(r_operand))

    def reset(self):
        self.variables: dict[str, int] = {
            "x": 0,
            "y": 0,
            "z": 0,
            "w": 0
        }

    def var_or_num(self, operand: str | int):
        if operand not in self.variables:
            return int(operand)
        else:
            return self.variables[operand]

def part1(code: str) -> str:
    alu = ALU(code)
    num = ""
    for i in range(14):
        z_collection: dict[int, int] = {}
        for j in range(1, 10):
            alu.run(num + str(j) + ("9"*(14-i)))
            z_collection[j] = alu.variables["z"]
            alu.reset()
        num += str(max(z_collection, key=z_collection.get))
    print(num)
    alu.run(num)
    vals = []
    for i in range(int(num) - 5_000_000, int(num) + 5_000_000):
        if "0" in str(i): continue
        alu.run(str(i))
        vals.append(alu.variables["z"])
        if alu.variables["z"] == 0:
            break
        alu.reset()
    else:
        print(f"Minimum val: {sorted(vals)[0]}")
        return "NONE"

    print(f"SOLUTION: {vals[-1]}")
    # num = 99999999999999
    # for i in range(num):
    #     if i % 100_000 == 0: print(f"iteration: {i}")
    #     if "0" in str(num):
    #         num -= 1
    #         continue
    #     alu.run(str(num))
    #     if alu.variables["z"] == 0:
    #         break
    #     alu.reset()

    # print(f"{num}: {alu.variables}")
    return num

def part2() -> str:
    pass

if __name__ == "__main__":
    output(
        part1(get_input()),
        part2()
    )
