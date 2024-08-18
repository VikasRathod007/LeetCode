# 2053. Kth Distinct String in an Array
def kthDistinct(arr, k):
    res = {}
    for s in arr:
        if s not in res:
            res[s] = 1
        else:
            res[s] += 1
    distinctElement = [s for s in res if res[s] == 1]
    return distinctElement[k - 1] if len(distinctElement) >= k else ""


arr = ["dbty"]
k = 1
print(kthDistinct(arr, k))  # Output: "a"
