from typing import Iterable, List, Set, Tuple

Matrix = List[List[int]]


def sudoku(matrix):
    while not solved(matrix):
        # TODO: solve
        pass
    return matrix


def solved(matrix: Matrix) -> bool:
    """
    Returns True if puzzle is solved, otherwise False.
    """
    return False


def missing(region: Iterable[int]) -> Set[int]:
    """
    Returns set of values missing in region (Iterable of 9 Integers).
    """
    return set()


def column(index: int, matrix: Matrix) -> Tuple:
    """
    Returns values in an index column in a matrix.
    """
    return ()


def square(row: int, column: int, matrix: Matrix) -> Tuple:
    """
    Returns values in a square delimited by row and column indexes.
    """
    return ()
