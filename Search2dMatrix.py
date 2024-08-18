# Go throw last element in a row and if < target then move to last element of next row
# if last element of a row is > target then scan entire if found return true else false


def searchMatrix(Matrix, Target):
    # Time complexit O(m*n)
    # row = len(Matrix)
    # col = len(Matrix[0])
    # for row in range(row):
    #     if Matrix[row][col - 1] == target:
    #         return True
    #     if Matrix[row][col - 1] > target:
    #         for cols in range(col):
    #             if Matrix[row][cols] == Target:
    #                 return True
    #         return False
    # return False
    # using binary search Time complexity O(log(m*n))
    # perform Binary search on sorted array
    if not Matrix:
        return False
    row = len(Matrix)
    col = len(Matrix[0])
    left, right = 0, row * col - 1
    while left <= right:
        mid = (left + right) // 2
        mid_val = Matrix[mid // col][mid % col]
        if mid_val == target:
            return True
        if mid_val > target:
            right = mid - 1
        else:
            left = mid + 1

    return False


matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
target = 10
print(searchMatrix(matrix, target))
