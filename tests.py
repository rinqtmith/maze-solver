import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),  # type: ignore[attr-defined]
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),  # type: ignore[attr-defined]
            num_rows,
        )

    def test_maze_constructor_attributes(self):
        m = Maze(1, 2, 3, 4, 5, 6)
        self.assertEqual(m._Maze__x1, 1)  # type: ignore[attr-defined]
        self.assertEqual(m._Maze__y1, 2)  # type: ignore[attr-defined]
        self.assertEqual(m._Maze__num_rows, 3)  # type: ignore[attr-defined]
        self.assertEqual(m._Maze__num_cols, 4)  # type: ignore[attr-defined]
        self.assertEqual(m._Maze__cell_size_x, 5)  # type: ignore[attr-defined]
        self.assertEqual(m._Maze__cell_size_y, 6)  # type: ignore[attr-defined]
        self.assertIsNone(m._Maze__win)  # type: ignore[attr-defined]

    def test_maze_cells_structure(self):
        num_rows = 3
        num_cols = 2
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m._Maze__cells), num_cols)  # type: ignore[attr-defined]
        for col in m._Maze__cells:  # type: ignore[attr-defined]
            self.assertEqual(len(col), num_rows)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._Maze__cells[0][0].has_top_wall,  # type: ignore[attr-defined]
            False,
        )
        self.assertEqual(
            m1._Maze__cells[num_cols - 1][num_rows - 1].has_bottom_wall,  # type: ignore[attr-defined]
            False,
        )


if __name__ == "__main__":
    unittest.main()
