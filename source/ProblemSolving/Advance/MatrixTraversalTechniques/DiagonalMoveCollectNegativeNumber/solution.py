def solution(matrix):
    rows, cols = len(matrix), len(matrix[0])
    negativeElementList = []
    if rows == 0 or cols == 0:
        return negativeElementList

    row, col = 0, 0
    up = True

    for _ in range(rows * cols):
        if matrix[row][col] < 0:
            negativeElementList.append((row, col))

        # move up right
        if up:
            newRow = row - 1
            newCol = col + 1
            if newRow < 0 or newCol >= cols:
                up = False
                # Hit right boundary
                if newCol >= cols:
                    row += 1
                # Hit top boundary
                else:
                    col += 1
            else:
                row = newRow
                col = newCol
        # move down left
        else:
            newRow = row + 1
            newCol = col - 1
            if newRow >= rows or newCol < 0:
                up = True
                # Hit bottom boundary
                if newRow >= rows:
                    col += 1
                # Hit right boundary
                else:
                    row += 1
            else:
                row = newRow
                col = newCol

    return negativeElementList
