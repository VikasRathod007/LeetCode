def maxDistance(positions, m):
    position.sort()
    length = len(position) - 1
    if m == 2 and length >= 2:
        return abs(position[0] - position[length])

    def canPlaceBalls(mid):
        count = 1
        last_pos = position[0]
        for i in range(1, len(position)):
            if position[i] - last_pos >= mid:
                count += 1
                last_pos = position[i]
                if count == m:
                    return True
        else:
            return False

    left, right = 1, position[-1] - position[0]
    best = 0
    while left <= right:
        mid = (left + right) // 2
        if canPlaceBalls(mid):
            best = mid
            left = mid + 1
        else:
            right = mid - 1
    return best


position = [1, 2, 3, 4, 7]
m = 3
print(maxDistance(position, m))
