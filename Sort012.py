def sort012(arr):
    # z_count = 0
    # o_count = 0
    # t_count = 0
    # for i in arr:
    #     if i == 0:
    #         z_count += 1
    #     elif i == 1:
    #         o_count += 1
    #     else:
    #         t_count += 1
    # return [0] * z_count + [1] * o_count + [2] * t_count
    low, i, high = 0, 0, len(arr) - 1
    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
            i += 1
        elif arr[i] == 2:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1
        else:
            i += 1
    return arr


arr = [0, 1, 2, 0, 1, 2]
print(sort012(arr))
