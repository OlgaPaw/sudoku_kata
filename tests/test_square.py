import pytest

from src.sudoku import square
from tests.values import PUZZLE, SOLUTION


@pytest.mark.parametrize(
    "matrix, row, column, value",
    (
        (PUZZLE, 0, 1, (5, 3, 0, 6, 0, 0, 0, 9, 8)),
        (SOLUTION, 4, 7, (5, 3, 7, 4, 1, 9, 2, 8, 6)),
        (SOLUTION, 7, 4, (4, 2, 3, 7, 9, 1, 8, 5, 6)),
    ),
)
def test_square(matrix, row, column, value):
    assert square(row, column, matrix) == value

