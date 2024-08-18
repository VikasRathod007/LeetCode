def maxArea(heights):
    left, right = 0, len(heights) - 1
    max_area = 0
    while left < right:
        width = right - left
        current_height = min(heights[left], heights[right])
        current_area = current_height * width
        max_area = max(max_area, current_area)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(maxArea(height))
