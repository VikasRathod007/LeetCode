def leader(arr):
    leader = []
    max_ = float("-inf")
    # for i in range(len(arr) - 1):
    #     if arr[i] >= max(arr[i + 1 :]):
    #         leader.append(arr[i])
    # leader.append(arr[-1])
    # return leader
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] >= max_:
            leader.append(arr[i])
            max_ = arr[i]
    leader.reverse()
    return leader


arr = [16, 17, 4, 3, 5, 2]
print(leader(arr))
