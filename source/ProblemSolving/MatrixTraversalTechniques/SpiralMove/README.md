Consider a grid of characters in the form of a 2D array, where each cell represents a distinct character selected from
a-z. Your task is to process this grid following a specific order.

Start from the top-left cell of the grid and move in a clockwise spiral direction. Initially, go right until you hit the
right boundary, then down until you reach the bottom boundary, then left until you encounter the left boundary, and
finally, up until you hit the top boundary (note that the top boundary is now the first row since we already visited the
first cell in the matrix). Once this cycle is complete, move inwards, i.e., one cell to the right, and repeat the spiral
process within the remaining unvisited cells.

During this spiral traversal, you will generate a sequence of visited cell characters. Afterwards, identify the vowels (
a, e, i, o, u) in the sequence and return their positions.

Please implement the function spiral_traverse_and_vowels(grid) to achieve this. This function takes a 2D array of
characters (grid) as input and returns a list containing the positions of the vowels in the spirally traversed sequence.

For instance, consider the following 3x4 grid:

```aiignore
[['a', 'b', 'c', 'd'],
['e', 'f', 'g', 'h'],
['i', 'j', 'k', 'l']]
```

Upon completing the spiral traversal, we will obtain the
sequence: ['a', 'b', 'c', 'd', 'h', 'l', 'k', 'j', 'i', 'e', 'f', 'g']. From this sequence, we observe that 'a', 'i',
and 'e' are vowels and are located at the 1st, 9th, and 10th positions in the sequence, so our function
returns: [0, 8, 9].

The size of the 2D array (grid) will not exceed 100x100, and each character will be a lowercase letter from 'a' to 'z'.