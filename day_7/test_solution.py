import unittest
import solution

def get_example_output() -> dict:
    tmp: list[str]
    with open("day_7/example_output.txt") as f:
        tmp = f.read().replace("\n","").replace(" ","").split(",")
    return {
        "part1": tmp[0],
        "part2": tmp[1]
    }

example_output = get_example_output()

class TestSolution(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(
            str(solution.part1(solution.get_input(example=True))), 
            example_output["part1"]
        )
    
    def test_part2(self):
        self.assertEqual(
            str(solution.part2(solution.get_input(example=True))), 
            example_output["part2"]
            )

if __name__ == "__main__":
    unittest.main()