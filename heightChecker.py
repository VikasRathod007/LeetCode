def heightChecker(heights):
    expected = sorted(heights)
    count = 0
    for i in range(len(expected)):
        if expected[i] != heights[i]:
            count += 1
    return count
    # count = 0
    # max_seen = float("-inf")
    # for height in heights:

    #     if height < max_seen:
    #         count += 1
    #     else:
    #         max_seen = height
    # return count


heights = [1, 1, 4, 2, 1, 3]
print(heightChecker(heights))
