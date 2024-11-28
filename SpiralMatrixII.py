def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    # print(matrix)
    val = 1
    left, right = 0, n - 1
    top, down = 0, n - 1

    while left <= right:
        for c in range(left, right + 1):
            matrix[top][c] = val
            print(val)
            val += 1
        top += 1
        for r in range(top, down + 1):
            matrix[r][right] = val
            print(val)
            val += 1

        right -= 1
        for c in range(right, left - 1, -1):
            matrix[down][c] = val
            print(val)
            val += 1
        down -= 1
        for r in range(down, top - 1, -1):
            matrix[r][left] = val
            print(val)
            val += 1
        left += 1
    return matrix


n = 3
print(generateMatrix(n))
