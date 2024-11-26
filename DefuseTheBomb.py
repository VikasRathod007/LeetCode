def decrypt(code, k):
    res = []
    n = len(code)
    if k == 0:
        return [0] * n
    elif k > 0:
        for i in range(n):
            temp = 0
            for j in range(1, k + 1):
                temp += code[(i + j) % n]
            res.append(temp)
        return res
    elif k < 0:
        for i in range(n):
            temp = 0
            for j in range(1, abs(k) + 1):
                temp += code[(i - j + n) % n]
            res.append(temp)
        return res


code = [2, 4, 9, 3]
k = -2
print(decrypt(code, k))
