from collections import Counter


# def MatrixScore(grid):
#     n = 0
#     sum = 0
#     gridIndex = 0
#     if grid[0][0] == 0:
#         for i in range(len(grid[gridIndex])):
#             if grid[0][i] == 0:
#                 grid[0][i] = 1
#             else:
#                 grid[0][i] = 0
#     counts = Counter(tuple(grid[gridIndex]))
#     # if counts[0] <= counts[1]:
#     for i in range(len(grid[gridIndex])):
#         if grid[0][i] == 0:
#             for j in range(len(grid)):
#                 # grid[j][i] = 1 if grid[j][i] == 0 else 0
#                 if grid[j][i] == 0:
#                     grid[j][i] = 1
#                 else:
#                     grid[j][i] = 0
#     for row in grid:
#         row_string = "".join(map(str, row))
#         sum += int(row_string, 2)
#     print(grid)
#     print(sum)


# matrix = [[0, 1], [0, 0]]
# MatrixScore(matrix)
# # binary = "01"
# # print(int(binary, 2))
# # for row in matrix:
# #     row_string = "".join(map(str, row))
# #     print(row_string)


def MatrixScore(grid):
    sum = 0
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        if grid[i][0] == 0:
            for c in range(cols):
                grid[i][c] = 1 if grid[i][c] == 0 else 0
    for c in range(1, cols):
        counts = Counter(row[c] for row in grid)
        if counts[0] > counts[1]:
            for r in range(rows):
                grid[i][c] = 1 if grid[i][c] == 0 else 0
    for row in grid:
        row_string = "".join(map(str, row))
        sum += int(row_string, 2)
    print(sum)
    print(grid)


matrix = [[0, 1], [1, 1]]
MatrixScore(matrix)
