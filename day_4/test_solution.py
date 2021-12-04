import unittest
import solution

def get_example_output() -> dict:
    tmp: list[str]
    with open("day_4/example_output.txt") as f:
        tmp = f.read().replace("\n","").replace(" ","").split(",")
    return {
        "part1": tmp[0],
        "part2": tmp[1]
    }

example_output = get_example_output()

class TestSolution(unittest.TestCase):
    def test_part1(self):
        bingo_numbers, bingo_fields = solution.get_input(example=True)
        self.assertEqual(
            str(solution.part1(bingo_numbers, bingo_fields)), 
            example_output["part1"]
        )
    
    def test_part2(self):
        bingo_numbers, bingo_fields = solution.get_input(example=True)
        self.assertEqual(
            str(solution.part2(bingo_numbers, bingo_fields)), 
            example_output["part2"]
            )

    def test_bingo_field_winning_checker(self):
        self.assertFalse(solution.BingoField(
            [
                ["!", "!", "!", "!", "!"],
                ["!", "!", "!", "!", "!"],
                ["!", "!", "!", "!", "!"],
                ["!", "!", "!", "!", "!"],
                ["!", "!", "!", "!", "!"],
            ]
        ).has_won())

        for i in range(0, 5):
            # == [ Test horizontally ] ==
            field1 = [
                ["!", "!", "!", "!", "!"],
                ["!", "!", "!", "!", "!"],
                ["!", "!", "!", "!", "!"],
                ["!", "!", "!", "!", "!"],
                ["!", "!", "!", "!", "!"],
            ]
            field1[i] = ["*", "*", "*", "*", "*"]
            self.assertTrue(solution.BingoField(field1).has_won())

            # == [ Test vertically ] ==
            field2 = [
                ["!", "!", "!", "!", "!"],
                ["!", "!", "!", "!", "!"],
                ["!", "!", "!", "!", "!"],
                ["!", "!", "!", "!", "!"],
                ["!", "!", "!", "!", "!"],
            ]
            for j in range(0, 5):
                field2[j][i] = "*"

            self.assertTrue(solution.BingoField(field2).has_won())

    def test_bingo_marker(self):
        b = solution.BingoField(
            [
                ["1", "2", "3", "4", "5"],
                ["6", "7", "8", "9", "10"],
                ["11", "12", "13", "14", "15"],
                ["16", "17", "18", "19", "20"],
                ["21", "22", "23", "24", "25"],
            ]
        )
        b.mark_number("12")
        self.assertEqual("*", b.field[2][1])
        
        b.mark_number("19")
        self.assertEqual("*", b.field[3][3])

    def test_bingo_unmarked_numbers(self):
        b = solution.BingoField(
            [
                ["1", "2", "3", "4", "5"],
                ["6", "7", "8", "*", "10"],
                ["*", "12", "13", "14", "*"],
                ["16", "*", "18", "19", "20"],
                ["21", "22", "*", "24", "*"],
            ]
        )
        self.assertEqual(sum(b.get_unmarked_numbers_as_int()), 225)

if __name__ == "__main__":
    unittest.main()