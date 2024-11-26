def majorityElement(arr):
    if len(arr) == 1:
        return arr[0]

    candidate = 0
    count = 0
    for i in arr:
        if count == 0:
            candidate = i
            # count += 1
        count += 1 if i == candidate else -1
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return -1


arr = [2, 13]
print(majorityElement(arr))
