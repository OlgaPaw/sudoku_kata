import pytest

from src.sudoku import column
from tests.values import puzzle, solution


@pytest.mark.parametrize(
    "matrix, index, value",
    (
        (puzzle(), 0, (5, 6, 0, 8, 4, 7, 0, 0, 0)),
        (solution(), 7, (1, 4, 6, 2, 9, 5, 8, 3, 7)),
    ),
)
def test_column(matrix, index, value):
    assert column(index, matrix) == value

