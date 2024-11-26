def getSecondLargest(arr):
    max_ = float("-inf")
    sec_max_ = float("-inf")
    for i in arr:
        if i > max_:
            max_, sec_max_ = sec_max_, i
        elif i < max_ and i > sec_max_:
            sec_max_ = i
    return sec_max_ if sec_max_ != float("-inf") else -1


arr = [12, 35, 1, 10, 34, 1]
print(getSecondLargest(arr))
