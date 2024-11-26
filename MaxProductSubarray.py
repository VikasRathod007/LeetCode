def maxProduct(arr):
    if not arr:
        return 0
    max_ = arr[0]
    min_ = arr[0]
    res = arr[0]
    for i in range(1, len(arr)):
        num = arr[i]
        if num < 0:
            min_, max_ = max_, min_
        max_ = max(num, max_ * num)
        min_ = min(num, min_ * num)
        res = max(res, max_)
    return res


arr = [-2, 6, -3, -10, 0, 2]
print(maxProduct(arr))
