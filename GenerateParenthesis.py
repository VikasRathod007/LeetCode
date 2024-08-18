import time


def generateParenthesis(n):
    stack = []
    res = []

    # def helper(openN, closeN):
    #     if openN == closeN == n:
    #         # print(f"Added stack to res {stack}")
    #         res.append("".join(stack))
    #         return
    #     if openN < n:
    #         stack.append("(")
    #         # print(f"after append openN < n {stack}")
    #         helper(openN + 1, closeN)
    #         # print(f"after helper openN < n {stack}")
    #         stack.pop()
    #     if closeN < openN:
    #         stack.append(")")
    #         # print(f"after append closeN < openN{stack}")
    #         helper(openN, closeN + 1)
    #         # print(f"after helper closeN < openN {stack}")
    #         stack.pop()
    def backtracking(current, openN, closeN):
        if openN == closeN == n:
            res.append(current)
            return
        if openN < n:
            backtracking(current + "(", openN + 1, closeN)
        if closeN < openN:
            backtracking(current + ")", openN, closeN + 1)

    backtracking("", 0, 0)

    # helper(0, 0)
    return res


n = 3
print(generateParenthesis(n))
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# stop when close==open==n
# add ')' when  close is less then open i.e  '(' < ')'
# add '(' if  '(' <n
