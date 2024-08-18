def productExceptSelf(nums):
    pre = 1
    post = 1

    num = [1] * (len(nums))

    for i in range(len(nums)):
        num[i] = pre
        pre *= nums[i]
    for i in range(len(nums) - 1, -1, -1):
        num[i] *= post
        post *= nums[i]
    return num


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
