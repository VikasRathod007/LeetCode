def trap(heights):
    n = len(heights)
    max_left = [0] * n
    max_right = [0] * n
    max_left[0] = heights[0]
    for i in range(1, n):
        max_left[i] = max(heights[i], max_left[i - 1])
    max_right[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(heights[i], max_right[i + 1])
    print(max_left)
    print(max_right)
    trapped_water = 0
    for i in range(n):
        trapped_water += min(max_right[i], max_left[i]) - height[i]
    return trapped_water


height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
print(trap(height))
