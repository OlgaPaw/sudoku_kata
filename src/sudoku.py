from typing import Iterable, List, Set, Tuple

Matrix = List[List[int]]


def sudoku(matrix):
    while not solved(matrix):
        # TODO: solve
        pass
    return matrix


def solved(matrix: Matrix) -> bool:
    return False


def missing(region: Iterable[int]) -> Set[int]:
    return set()


def column(index: int, matrix: Matrix) -> Tuple:
    return ()


def square(row: int, column: int, matrix: Matrix) -> Tuple:
    return ()
