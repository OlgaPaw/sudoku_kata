import pytest

from src.sudoku import column
from tests.values import PUZZLE, SOLUTION


@pytest.mark.parametrize(
    "matrix, index, value",
    (
        (PUZZLE, 0, (5, 6, 0, 8, 4, 7, 0, 0, 0)),
        (SOLUTION, 7, (1, 4, 6, 2, 9, 5, 8, 3, 7)),
    ),
)
def test_column(matrix, index, value):
    assert column(index, matrix) == value

