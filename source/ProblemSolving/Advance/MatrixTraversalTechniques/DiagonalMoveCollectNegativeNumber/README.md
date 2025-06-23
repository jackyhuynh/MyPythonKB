Given a 2D matrix of n x m integers, where n represents the number of rows and m represents the number of columns. Both
n and m range from 1 to 100, inclusive.

The matrix cells may contain either a positive, a negative integer, or zero, with values ranging from -100 to 100,
inclusive.

In this task, you are required to traverse the matrix diagonally from the top-left cell to the bottom-right cell in a
zigzag pattern. Start from the top-left cell, move one cell to the right (if it exists), then move one step diagonally
down-left. After reaching a left (bottom) boundary, move one step down (right) and start moving diagonally up-right.
Continue this pattern until you reach the last cell of the matrix. Your task is to return a list of tuples, each tuple
containing the index pair of cells with negative integers encountered during your traversal.

For example, consider a 3 x 4 matrix:

``` python
[[1, -2, 3, -4],
[5, -6, 7, 8],
[-9, 10, -11, 12]]
```

The traversal in a zigzag pattern will result in: [1, -2, 5, -9, -6, 3, -4, 7, 10, -11, 8, 12]

The negative integers in this sequence and their corresponding positions in the matrix are: [-2, -9, -6, -4, -11], with
indices: [(0, 1), (2, 0), (1, 1), (0, 3), (2, 2)].

Your function, solution(matrix), should then return these indices as a list of
tuples: [(0, 1), (2, 0), (1, 1), (0, 3), (2, 2)].