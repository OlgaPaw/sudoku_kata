import pytest

from src.sudoku import sudoku
from tests.values import puzzle, solution


@pytest.mark.timeout(5)
def test_solution():
    assert sudoku(puzzle()) == solution()

