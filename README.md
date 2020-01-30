# Sudoku Solver Kata

https://www.codewars.com/kata/5296bc77afba8baa690002d7

Usage:

Fill sudoku.py and run tests!
Ensure you are running from virtualenv and have `pytest-timeout` installed.
Otherwise, test will hang.

Suggested test order:

1. `python -m pytest tests/test_unit`
2. `python -m pytest tests/test_solution.py`
3. `python -m pytest tests/test_full.py`

# Tasks

1. Implement `solved`, `missing`, `column` and `square` methods
1. Implement algorithm: while not solved iterate over items to find cells that have only one possible value. Fill this value and iterate again.
1. Use set comprehension anywhere
1. Use generator anywhere
1. Use `zip` to get matrix column
1. Use `itertools.chain`
1. Use `yield from`
