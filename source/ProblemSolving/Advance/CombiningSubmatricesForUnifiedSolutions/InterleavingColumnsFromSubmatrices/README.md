Your task is to write a function, interleave_matrices(), that takes two matrices (2D arrays) and a start and end range
for rows and columns for each matrix as inputs. Instead of concatenating submatrices together, this task requires
interleaving the columns from the submatrices within the final matrix.

If A and B are your two matrices, and the respective submatrices selected from them based on the given ranges are sub_A
and sub_B, then the task is to form a new matrix C by interleaving columns from sub_A and sub_B. Starting with the first
column of sub_A, alternately include a column from sub_A and a column from sub_B until all columns from both submatrices
are included.

For example, if A is:

```python
[[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]]
```

and B is:

```python
[[11, 12, 13],
[14, 15, 16],
[17, 18, 19]]
```

If we select 2x2 submatrices from each (comprising the 2nd to the 3rd rows and the 2nd to the 3rd columns from A, and
the 1st to the 2nd rows and the 1st to the 2nd columns from B), their interleaved combination would look like this:

Copy to clipboard

```python
[[6, 11, 7, 12],
[10, 14, 11, 15]]
```

Note that in the output, columns from sub_A and sub_B are interwoven.

It is guaranteed that the given submatrices have pairwise equal dimensions.