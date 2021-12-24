import unittest
import solution

def get_example_output() -> dict:
    return {}
    tmp: list[str]
    with open("day_24/example_output.txt") as f:
        tmp = f.read().replace("\n","").replace(" ","").split(",")
    return {
        "part1": tmp[0],
        "part2": tmp[1]
    }

example_output = get_example_output()

class TestSolution(unittest.TestCase):
    def _test_part1(self):
        self.assertEqual(
            str(solution.part1(solution.get_input(example=True))), 
            example_output["part1"]
        )
    
    def _test_part2(self):
        self.assertEqual(
            str(solution.part2(solution.get_input(example=True))), 
            example_output["part2"]
            )

class TestALU(unittest.TestCase):
    def test_interpreter(self):
        code = "add x 5\nadd z 20\ndiv z 5\nmod x z\nmul x 4\neql z x"
        alu = solution.ALU(code)
        alu.run()
        self.assertEqual(
            alu.variables["z"],
            1
        )

if __name__ == "__main__":
    unittest.main()