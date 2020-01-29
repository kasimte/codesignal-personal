# Sudoku 2

[Problem on CodeSignal](https://app.codesignal.com/interview-practice/task/SKZ45AF99NpbnvgTn)

This is a sudoku board validity checker. The `sudoku2` function takes
in a 9x9 `grid` (an array of arrays) and outputs True or False
depending on whether it is valid or not.

The approach here splits up the validity into three components, each
of which has to be valid:

* rows
* columns
* 3x3 boxes

## Notes

* `list(zip(*grid))` is a handy way to turn the grid rows into
  columns. The `*` operator unfolds the array into a list of
  parameters for the `zip` function, which returns an `iterable`,
  which is then transformed back into an array with the `list`
  operator.
  
* If you have a hash of counts, you can pull out the key of the max
  value like so:

```
>>> counts = {5: 1, 8: 2, 9: 1}
>>> max(counts, key=counts.get)
8
```

## Example of * in Python

```
grid = [[1, 2], [3, 4], [5, 6]]
zip(*grid) # this is the same as calling zip([1,2], [3,4], [5,6])
zip(grid) # this is zip([[1, 2], [3, 4], [5, 6]])
```
