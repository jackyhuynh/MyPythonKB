def submatrix_swap(matrix, coord_S1, coord_S2):
    # submatrix_swap(matrix, coord_S1=[0, 2, 2, 4], coord_S2=[2, 4, 0, 2])
    # M =  [[1, 2, 3, 4, 5],
    #       [6, 7, 8, 9, 10],
    #       [11, 12, 13, 14, 15],
    #       [16, 17, 18, 19, 20],
    #       [21, 22, 23, 24, 25]]
    #       row1 = 0, 1
    #       col1 = 2, 3
    #       row2 = 2, 3
    #       col1 = 0, 1
    #      [[1, 2, 11, 12, 5],
    #       [6, 7, 16, 17, 10],
    #       [3, 4, 13, 14, 15],
    #       [8, 9, 18, 19, 20],
    #       [21, 22, 23, 24, 25]]

    def get_submatrix(matrix, coord):
        submatrix = []
        start_row, end_row, start_col, end_col = coord
        for row in range(start_row, end_row):
            submatrix.append(matrix[row][start_col:end_col])
        return submatrix

    def set_submatrix(matrix, submatrix, coord):
        start_row, end_row, start_col, end_col = coord
        for i, row in enumerate(submatrix):
            print(f"Setting row {i} of submatrix at matrix[{start_row + i}][{start_col}:{end_col}]")
            for j, value in enumerate(row):
                print(f"Setting matrix[{start_row + i}][{start_col + j}] = {value}")
                matrix[start_row + i][start_col + j] = value
        return matrix

    submatrix1 = get_submatrix(matrix, coord_S1)
    submatrix2 = get_submatrix(matrix, coord_S2)
    # Swap the submatrices
    matrix = set_submatrix(matrix, submatrix2, coord_S1)
    matrix = set_submatrix(matrix, submatrix1, coord_S2)
    return matrix
