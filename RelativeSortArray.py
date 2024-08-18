def relativeSortArray(arr1, arr2):
    map_ = {}
    res = []
    for num in arr1:
        if num in map_:
            map_[num] += 1
        else:
            map_[num] = 1
    for i in arr2:
        count = map_[i]
        for j in range(count):
            res.append(i)
        del map_[i]
    remaining_element = sorted(map_.keys())
    for elem in remaining_element:
        count = map_[elem]
        for _ in range(count):
            res.append(elem)
    return res


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
print(relativeSortArray(arr1, arr2))
