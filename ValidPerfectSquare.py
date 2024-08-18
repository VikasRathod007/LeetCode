def isPerfectSquare(n):
    for i in range(n):
        if n == 1:
            return True
        if i * i == n:
            return True
        elif i * i > n:
            return False


n = 1
print(isPerfectSquare(n))
