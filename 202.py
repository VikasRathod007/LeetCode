# 202. Happy Number
# https://leetcode.com/problems/happy-number/
def isHappy(n):
    def helper(n):
        s = 0
        while n > 0:
            x = n % 10
            s += x * x
            n = n // 10
        return s

    visited = set()
    i = 0
    while n != 1 and n not in visited:
        visited.add(n)
        n = helper(n)
    if n == 1:
        return True

    # while True:
    #     if n == 1:
    #         return True

    #     i += 1
    #     n = helper(n)
    #     if n in visited:
    #         return False
    #     visited.add(n)


n = 19
print(isHappy(n))
