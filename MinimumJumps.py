def minJumps(arr):
    n = len(arr)
    if arr[0] == 0:
        return -1
    if n == 1:
        return 0
    max_ = arr[0]
    jump = 1
    step = arr[0]
    for i in range(1, len(arr)):
        if i == len(arr) - 1:
            return jump
        max_ = max(max_, i + arr[i])
        step -= 1
        if step == 0:
            jump += 1
            if i >= max_:
                return -1
            step = max_ - i
    return -1


arr = [1, 2, 3, 1, 6, 7]
print(minJumps(arr))
