You are tasked with creating a Python function named matrix_boundary_concatenation(). This function should accept two 2D
matrices, matrix_A and matrix_B, and the number of boundary layers, n, to extract from both matrices.

In this context, a boundary layer refers to the elements that form the outer contour of a matrix. For instance, the
first layer of the following 4x4 matrix includes the elements 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, and 5:

Python

```
[[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]]
```

Your function should extract the first n boundary layers from both matrix_A and matrix_B. It should then concatenate
these extracted layers into a new array, ensuring that the layers from matrix_A precede those from matrix_B in the
resultant array.

The matrices A and B will be square matrices, with each side's length ranging from 1 to 10. The number of layers n will
be less than or equal to the side length of the square matrices.

The function signature should be:

```python
def matrix_boundary_concatenation(matrix_A, matrix_B, n):
```

The elements in the input matrices can be any integer between -100 and 100.

Example

Consider the following input to our function:

```python
matrix_A = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]
```

```python
matrix_B = [[17, 18, 19, 20],
            [21, 22, 23, 24],
            [25, 26, 27, 28],
            [29, 30, 31, 32]]
```

n = 2
Our function matrix_boundary_concatenation(matrix_A, matrix_B, n) should return:

```python
[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10, 17, 18, 19, 20, 24, 28, 32, 31, 30, 29, 25, 21, 22, 23, 27, 26]
```

Explanation:

In matrix_A, the first boundary layer is composed of the elements 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, and 5, taken in
a clockwise direction from the top-left corner. Our second layer then includes the elements 6, 7, 11, and 10.

For matrix_B, the corresponding boundary layers include the elements 17, 18, 19, 20, 24, 28, 32, 31, 30, 29, 25, 21 for
the first layer and 22, 23, 27, 26 for the second one.

The function outputs an array where the extracted layers from matrix_A are followed by those from matrix_B.