from collections import Counter


def TopKElements(nums, k):
    arr = Counter(nums)
    new_arr = []
    sorted_items = arr.most_common(k)
    new_arr = [arr[0] for arr in sorted_items]
    return new_arr


nums = [7, 4, 1, 7, 2, 1, 1, 1]
k = 3
print(TopKElements(nums, k))
