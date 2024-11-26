def findMajority(arr):
    hash_map = {}
    res = []
    n = len(arr)
    min_count = n // 3
    for i in range(n):
        if arr[i] in hash_map:
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    for i in hash_map.keys():
        if hash_map[i] > min_count:
            res.append(i)
    res.sort()
    return res


arr = [2, 1, 6, 6, 6, 6, 6, 5, 5, 5, 5]
print(findMajority(arr))
