import math


def judgeSquareSum(c):
    low = 0
    high = int(math.sqrt(c))
    while low <= high:
        ans = low**2 + high**2
        if ans == c:
            return True
        elif ans > c:
            high -= 1
        else:
            low += 1

    return False


print(judgeSquareSum(4))
