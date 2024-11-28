def myAtoi(s):
    res = 0
    sign = 1
    started = False
    max_ = 2**31 - 1
    min_ = -(2**31)

    for char in s:
        if not started and char == " ":
            continue
        if not started and (char == "+" or char == "-"):
            sign = -1 if char == "-" else 1
            started = True
            continue
        if char.isdigit():
            digit = int(char)

            res = res * 10 + digit
            started = True
        else:
            break
    res *= sign

    return max(min_, min(max_, res))
    # try:
    #     result = int(s.strip())
    #     print(result)
    #     max_ = 2**31 - 1
    #     min_ = -(2**31)
    #     return max(min_, min(max_, result))
    # except:
    #     return 0


s = "-0012gfg4"
print(myAtoi(s))
