from src.sudoku import solved
from tests.values import PUZZLE, SOLUTION


def test_solved():
    assert solved(SOLUTION) is True


def test_not_solved():
    assert solved(PUZZLE) is False
