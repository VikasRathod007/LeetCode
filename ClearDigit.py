def ClearDigit(s):
    i = 0
    s = list(s)
    while i < len(s):
        if s[i].isdigit():
            left = i
            right = i
            left = i - 1
            while left >= 0 and s[left].isdigit():
                left -= 1

            right = i + 1
            while right < len(s) and s[right].isdigit():
                right += 1
    return s


s = "vi123kas1h"
print(ClearDigit(s))
