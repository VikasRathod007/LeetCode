def pushZerosToEnd(arr):
    # count = 0
    # for i in arr:
    #     if i == 0:
    #         count += 1
    # for i in range(count):
    #     arr.remove(0)
    # for i in range(count):
    #     arr.append(0)
    # return arr
    # non_zeros = [x for x in arr if x != 0]
    # non_zeros.extend([0] * (len(arr) - len(non_zeros)))
    # return non_zeros
    zero_index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[zero_index], arr[i] = arr[i], arr[zero_index]
            zero_index += 1
    return arr


arr = [3, 5, 0, 0, 4]
print(pushZerosToEnd(arr))
