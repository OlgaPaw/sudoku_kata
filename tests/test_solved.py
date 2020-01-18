from src.sudoku import solved
from tests.values import puzzle, solution


def test_solved():
    assert solved(solution()) is True


def test_not_solved():
    assert solved(puzzle()) is False
