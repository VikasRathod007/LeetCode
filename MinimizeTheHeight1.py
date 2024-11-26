def getMinDiff(arr, k):
    arr.sort()
    n = len(arr)
    print(arr)
    diff = arr[n - 1] - arr[0]
    print(diff)
    for i in range(0, n - 1):
        min_ = min(arr[0] + k, arr[i + 1] - k)
        max_ = max(arr[i] + k, arr[n - 1] - k)
        print(min_, max_)
        diff = min(diff, max_ - min_)
        print(diff)
    return diff


arr = [1, 8, 10, 6, 4, 6, 9, 1]

k = 7
print(getMinDiff(arr, k))
