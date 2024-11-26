def rotateArr(arr, d):
    n = len(arr)
    d = d % n
    temp = arr[:d]
    for i in range(n - d):
        arr[i] = arr[i + d]
    for i in range(d):
        arr[n - d + i] = temp[i]
    return arr
    # res = []
    # return arr[d:] + arr[:d]
    # for i in range(d, n):
    #     res.append(arr[i])
    # for i in range(0, d):
    #     res.append(arr[i])
    # return res

    # for i in range(d):
    #     temp = arr[0]
    #     for j in range(1, n):
    #         arr[j - 1] = arr[j]
    #     arr[n - 1] = temp
    # return arr


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
d = 3
print(rotateArr(arr, d))
