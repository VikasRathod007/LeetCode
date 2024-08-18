def specialArray(nums):
    num = [i for i in nums if i != 0]
    if len(num) == 0:
        return -1
    num.sort()
    print(num)
    # for i in range(0, len(num)):
    #     x = num[i] - 1
    #     print(x)
    #     if x == len(num) - i or x + 1 == len(num):
    #         return x
    # return -1
    for i in range(0, len(num)):
        x = len(num) - i
        print(x)
        if num[i] >= x:
            if i == 0 or num[i - 1] < x:
                print("if")
                return x
    return -1


nums = [3, 6, 7, 7, 8, 10]
print(specialArray(nums))
