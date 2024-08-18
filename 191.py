# 191. Number of 1 Bits
def hammingWeight(n):
    binary = []
    while n >= 1:
        rem = n % 2
        n = n // 2
        binary.append(rem)
    # binary.append(1)
    print(binary)
    return binary.count(1)


n = 2147483645
print(hammingWeight(n))
f
