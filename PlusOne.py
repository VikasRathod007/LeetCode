def PlusOne(arr):
    # if arr[len(arr) - 1] < 9:
    #     arr[len(arr) - 1] += 1
    # else:
    #     arr[len(arr) - 1] = 1
    #     arr.append(0)
    # return arr
    total = "".join(map(str, arr))
    total = str(int(total) + 1)
    res_list = [int(digit) for digit in total]
    return res_list


digits = [4, 3, 2, 9]
print(PlusOne(digits))
