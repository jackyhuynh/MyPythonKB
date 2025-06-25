def solution(matrix_A, matrix_B, submatrix_coords):
    """
    Extracts specified submatrices from matrix_A and matrix_B,
    then interleaves their elements row by row to create a new matrix.

    Args:
        matrix_A (list of list of int): The first input matrix.
        matrix_B (list of list of int): The second input matrix.
        submatrix_coords (list of tuple): A list containing two tuples.
            - The first tuple (startRowA, endRowA, startColA, endColA) defines
              the 1-based coordinates for extracting a submatrix from matrix_A.
            - The second tuple (startRowB, endRowB, startColB, endColB) defines
              the 1-based coordinates for extracting a submatrix from matrix_B.

    Returns:
        list of list of int: A new matrix formed by interleaving the elements
                              of the extracted submatrices row by row.
                              e.g., for rows [a1, a2] and [b1, b2], the interleaved
                              row will be [a1, b1, a2, b2].
    """
    # Unpack the 1-based coordinates for submatrix A and submatrix B
    startRowA, endRowA, startColA, endColA = submatrix_coords[0]
    startRowB, endRowB, startColB, endColB = submatrix_coords[1]

    # Extract submatrixA using 0-based indexing for slicing.
    # Python's slice [start:end] includes 'start' but excludes 'end'.
    # Hence, 'startRowA - 1' is used for the start index, and 'endRowA' for the end.
    submatrixA = [row[startColA - 1: endColA] for row in matrix_A[startRowA - 1: endRowA]]

    # Extract submatrixB using 0-based indexing for slicing, similar to submatrixA.
    submatrixB = [row[startColB - 1: endColB] for row in matrix_B[startRowB - 1: endRowB]]

    # Interleave the elements of submatrixA and submatrixB row by row.
    # The outer list comprehension iterates through corresponding rows of submatrixA and submatrixB.
    # The inner list comprehension flattens zipped pairs of elements from each row,
    # effectively interleaving them: [a1, b1, a2, b2, ...].
    interleaved_matrix = [[elem for pair in zip(rowA, rowB) for elem in pair]
                          for rowA, rowB in zip(submatrixA, submatrixB)]

    return interleaved_matrix
