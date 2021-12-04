from copy import deepcopy

def get_input(example: bool = False) -> list[str]:
    """
    Returns the input of the input.txt file
    """
    inp = ""
    with open(f"day_4/{'example_' if example else ''}input.txt", "r") as f:
        inp = f.readlines()
    
    bingo_numbers: list[str] = inp[0].replace("\n","").split(",")
    bingo_fields: list[BingoField] = []
    
    for i in range(2, len(inp) - 2, 6):
        bingo_fields.append(
            BingoField(
                [
                    inp[i].replace("\n","").split(),
                    inp[i + 1].replace("\n","").split(),
                    inp[i + 2].replace("\n","").split(),
                    inp[i + 3].replace("\n","").split(),
                    inp[i + 4].replace("\n","").split(),
                ]
            )
        )

    return [bingo_numbers, bingo_fields]

def output(string1: str = "None", string2: str = "None") -> None:
    """
    Write the solution to both parts into the output file
    """
    with open("day_4/output.txt", "w") as f:
        f.write(f"Part 1:\n{string1}\n=========\nPart 2:\n{string2}")

class BingoField:
    def __init__(self, field) -> None:
        # Field Format("!" = Some char or number):
        # [
        #     ["!", "!", "!", "!", "!"],
        #     ["!", "!", "!", "!", "!"],
        #     ["!", "!", "!", "!", "!"],
        #     ["!", "!", "!", "!", "!"],
        #     ["!", "!", "!", "!", "!"]
        # ]
        self.field: list[list[str]] = field
    
    def has_won(self) -> bool:
        f = self.field
        for i in range(0, 5):
            # Case: vertically won
            if all([item == "*" for item in [f[x][i] for x in range(0, 5)]]):
                return True

            # Case: horizontally won
            elif all([item == "*" for item in f[i]]):
                return True

    def mark_number(self, num: str):
        for i in range(0, len(self.field)):
            for j in range(0, len(self.field[0])):
                if self.field[i][j] == num:
                    self.field[i][j] = "*"
                    return

    def get_unmarked_numbers_as_int(self) -> list[int]:
        all_items: list[str] = []
        for b in self.field:
            all_items += b
        
        return [int(x) for x in all_items if x != "*"]


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

if __name__ == "__main__":
    bingo_numbers, bingo_fields = get_input()

    output(
        part1(deepcopy(bingo_numbers), deepcopy(bingo_fields)),
        part2(deepcopy(bingo_numbers), deepcopy(bingo_fields))
    )