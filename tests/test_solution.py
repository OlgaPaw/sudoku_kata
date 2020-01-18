from src.sudoku import sudoku
from tests.values import puzzle, solution


def test_solution():
    assert sudoku(puzzle()) == solution()

