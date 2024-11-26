# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
def permuteUnique(nums):
    res = []
    # nums = list(set(nums))
    seen = set()
    if len(nums) == 1:
        return [nums[:]]
    for i in range(len(nums)):
        n = nums[i]
        if n in seen:
            continue
        seen.add(n)
        perms = permuteUnique(nums[:i] + nums[i + 1 :])
        for perm in perms:
            perm.append(n)
        res.extend(perms)
    return res


print(permuteUnique([1, 1, 2]))
