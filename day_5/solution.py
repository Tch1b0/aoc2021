class Coordinates():
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Coordinates):
            return self.x == __o.x and self.y == __o.y
        else:
            raise NotImplementedError()

    def __str__(self) -> str:
        return str((self.x, self.y))

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    @staticmethod
    def from_string(string: str):
        tmp = [int(x) for x in string.split(",")]
        return Coordinates(tmp[0], tmp[1])

class Vent():
    def __init__(self, from_coords: Coordinates, to_coords: Coordinates) -> None:
        self.diagonal: bool = False
        self.coords: list[Coordinates] = []

        # Case: Diagonal line
        if from_coords.x != to_coords.x and from_coords.y != to_coords.y: 
            self.diagonal = True
            start, end = (from_coords, to_coords) if from_coords.y < to_coords.y else (to_coords, from_coords)
            x: int = start.x
            increment = 1 if end.x > x else -1
            for y in range(start.y, end.y + 1):
                self.coords.append(Coordinates(x, y))
                x += increment
        # Case: Horizontal line
        elif from_coords.x != to_coords.x:
            for i in range(min(from_coords.x, to_coords.x), max(from_coords.x, to_coords.x) + 1):
                self.coords.append(Coordinates(i, from_coords.y))
        # Case: Vertical line
        else:
            for i in range(min(from_coords.y, to_coords.y), max(from_coords.y, to_coords.y) + 1):
                self.coords.append(Coordinates(from_coords.x, i))

        if len(self.coords) < 2:
            raise ValueError("Vent couldn't load coordinates")

    def __str__(self) -> str:
        return f"{self.coords[0].x, self.coords[0].y} -> {self.coords[-1].x, self.coords[-1].y}"

    def __repr__(self) -> str:
        return str(self)

    @staticmethod
    def from_string(string: str):
        tmp = string.replace(" ", "").split("->")
        return Vent(Coordinates.from_string(tmp[0]), Coordinates.from_string(tmp[1]))

class GameField():
    def __init__(self, vents: list[Vent] = []) -> None:
        self.vents: list[Vent] = vents

    def __str__(self) -> str:
        return str(self.vents)

    def plant_mine(self, vent: Vent) -> None:
        self.vents.append(vent)

    def count_overlapping_vents(self, diagonal: bool = False) -> int:
        field = {}
        
        for vent in self.vents:
            if vent.diagonal and not diagonal: continue
            for coord in vent.coords:
                if coord in field.keys():
                    field[coord] += 1
                else:
                    field[coord] = 1

        return len([x for x in field.values() if x > 1])

def get_input(example: bool = False) -> GameField:
    """
    Returns the input of the input.txt file
    """
    txt = ""
    with open(f"day_5/{'example_' if example else ''}input.txt", "r") as f:
        txt = [x for x in f.readlines()]
    
    return GameField([Vent.from_string(x) for x in txt])

def output(string1: str = "None", string2: str = "None") -> None:
    """
    Write the solution to both parts into the output file
    """
    with open("day_5/output.txt", "w") as f:
        f.write(f"Part 1:\n{string1}\n=========\nPart 2:\n{string2}")

def part1(game_field: GameField) -> int:
    return game_field.count_overlapping_vents(diagonal=False)

def part2(game_field: GameField) -> int:
    return game_field.count_overlapping_vents(diagonal=True)

if __name__ == "__main__":
    output(
        part1(get_input()),
        part2(get_input())
    )