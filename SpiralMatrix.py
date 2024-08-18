# 54. Spiral Matrix
def spiralOrder(nums):
    res = []
    n = len(nums)
    m = len(nums[0])
    top, bottom, left, right = 0, n - 1, 0, m - 1
    while top <= bottom and left <= right:
        # moving left to right
        for i in range(top, right + 1):
            res.append(nums[top][i])
        top += 1
        # moving top to down
        for i in range(right, bottom + 1):
            res.append(nums[i][right])
        right -= 1
        # for moving right to left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(nums[bottom][i])
            bottom -= 1

        # for moving bottom to top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(nums[i][left])
            left += 1
    return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiralOrder(matrix))
