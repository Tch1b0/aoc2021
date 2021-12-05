import unittest
import solution as s

def get_example_output() -> dict:
    tmp: list[str]
    with open("day_5/example_output.txt") as f:
        tmp = f.read().replace("\n","").replace(" ","").split(",")
    return {
        "part1": tmp[0],
        "part2": tmp[1]
    }

example_output = get_example_output()

class Tests(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(
            str(s.part1(s.get_input(example=True))), 
            example_output["part1"]
        )
    
    def test_part2(self):
        self.assertEqual(
            str(s.part2(s.get_input(example=True))), 
            example_output["part2"]
        )

    def test_Vent(self):
        m1 = s.Vent(
            s.Coordinates(1,5),
            s.Coordinates(3,5)
        )

        self.assertEqual(
            m1.coords,
            [s.Coordinates(1, 5), s.Coordinates(2, 5), s.Coordinates(3, 5)]
        )

        m2 = s.Vent(
            s.Coordinates(0,0),
            s.Coordinates(2,2)
        )

        self.assertEqual(
            m2.coords,
            [s.Coordinates(0, 0), s.Coordinates(1, 1), s.Coordinates(2, 2)]
        )

        m3 = s.Vent(
            s.Coordinates(3, 0),
            s.Coordinates(0, 3)
        )

        self.assertEqual(
            m3.coords,
            [s.Coordinates(3, 0), s.Coordinates(2, 1), s.Coordinates(1, 2), s.Coordinates(0, 3)]
        )

        m4 = s.Vent(
            s.Coordinates(5, 2),
            s.Coordinates(2, 5)
        )

        self.assertEqual(
            m4.coords,
            [s.Coordinates(5, 2), s.Coordinates(4, 3), s.Coordinates(3, 4), s.Coordinates(2, 5)]
        )

        m5 = s.Vent(
            s.Coordinates(3, 3),
            s.Coordinates(0, 0)
        )

        self.assertEqual(
            m5.coords,
            [s.Coordinates(0, 0), s.Coordinates(1, 1), s.Coordinates(2, 2), s.Coordinates(3, 3)]
        )

    def test_Gamefield(self):
        g = s.GameField(
            [
                s.Vent(s.Coordinates(1, 2), s.Coordinates(2, 2)),
                s.Vent(s.Coordinates(1, 2), s.Coordinates(2, 2))
            ]
        )

        self.assertEqual(g.count_overlapping_vents(), 2)

if __name__ == "__main__":
    unittest.main()