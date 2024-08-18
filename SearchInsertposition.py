def searchInsert(arr, n):
    if arr.count(n) >= 1:
        return arr.index(n)
    else:
        for i in range(len(arr)):
            if arr[i] > n:
                print(i)
                return i
    return len(arr)


nums = [1, 3, 5, 5, 6]
target = 8
print(searchInsert(nums, target))
