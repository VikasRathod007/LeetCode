def scoreOfString(s):
    res = 0
    for i in range(len(s) - 1):
        res += abs(ord(s[i]) - ord(s[i + 1]))
    return res


s = "hello"
print(scoreOfString(s))  # Output: 532
