import unittest
import solution

def get_example_output() -> dict:
    tmp: list[str]
    with open("day_9/example_output.txt") as f:
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
    
    def test_part2(self):
        self.assertEqual(
            str(solution.part2(solution.get_input(example=True))), 
            example_output["part2"]
            )
    
    def test_basin_collection(self):
        bc = solution.BasinCollection([solution.Basin([(1, 2), (2, 2)]), solution.Basin([(3, 4), (4, 4)])])
        self.assertEqual(
            bc.basins[0].size(),
            2
        )
        self.assertEqual(
            bc.basins[1].size(),
            2
        )
        self.assertEqual(
            bc.basins[0].size() * bc.basins[1].size(),
            4
        )
        self.assertEqual(
            len(bc.basins[:2]),
            2
        )
        
        self.assertEqual(
            bc.get_top_sum(2),
            4
        )

if __name__ == "__main__":
    unittest.main()