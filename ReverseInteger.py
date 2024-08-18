def Reverse(num):
    rev = 0
    sign = 1 if num >= 0 else -1
    num = abs(num)
    while num > 0:
        a = num % 10
        rev = rev * 10 + a
        num = num // 10
    if (-2147483648) <= num <= (2147483647):
        return sign * rev
    else:
        return 0


x = -123
print(Reverse(x))
