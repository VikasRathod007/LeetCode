def multiply(num1, num2):
    carry = 0
    res = [0] * (len(num1) + len(num2))
    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            prod = (int(num1[i]) * int(num2[j])) + carry + res[i + j + 1]
            res[i + j + 1] = prod % 10
            carry = prod // 10
        res[i + j] += carry
        carry = 0
    return "".join(map(str, res)).lstrip("0") or "0"


num1 = "2"
num2 = "3"
print(multiply(num1, num2))
