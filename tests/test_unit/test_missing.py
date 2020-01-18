from src.sudoku import missing


def test_not_missing():
    assert missing(range(0, 10)) == set()


def test_missing():
    assert missing([1, 2, 3, 6, 7, 8]) == {4, 5, 9}
