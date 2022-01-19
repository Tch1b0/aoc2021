def get_input(example: bool = False) -> str:
    """
    Returns the input of the input.txt file
    """
    with open(f"day_15/{'example_' if example else ''}input.txt", "r") as f:
        content = [[int(col) for col in row if col != "\n"]
                   for row in f.readlines()]

    return content


def output(string1: str = "None", string2: str = "None") -> None:
    """
    Write the solution to both parts into the output file
    """
    with open("day_15/output.txt", "w") as f:
        f.write(f"Part 1:\n{string1}\n=========\nPart 2:\n{string2}")

safest_moves = 700
def find_path(matrix: list[list[int]],
              coords: tuple[int, int],
              move_history: list[int],
              depth: int = 0
              ) -> int:
    global safest_moves

    move_history.append(matrix[coords[1]][coords[0]])

    # Path finder has finished?
    if coords == (len(matrix[0]) - 1, len(matrix) - 1):
        if (tmp := sum(move_history)) < safest_moves or safest_moves == -1:
            safest_moves = tmp
            print(tmp)
        return tmp

    # Path finders path is too 'expensive'
    elif sum(move_history) >= safest_moves and safest_moves != -1:
        return sum(move_history)

    else:
        tmp = []
        if coords[0] != len(matrix[0]) - 1:
            tmp.append(find_path(matrix, (coords[0] + 1, coords[1]), move_history.copy(), depth + 1))
        if coords[1] != len(matrix) - 1:
            tmp.append(find_path(matrix, (coords[0], coords[1] + 1), move_history.copy(), depth + 1))

        return min(tmp)


def part1(matrix) -> int:
    return find_path(matrix, (0, 0), []) - 1


def part2() -> str:
    pass


if __name__ == "__main__":
    output(
        part1(get_input()),
        part2()
    )
