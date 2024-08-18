from collections import Counter


def isvalid(s):

    s = list(s)

    # for i in range(0, len(s) - 1, 2):
    #     if (
    #         s[i] == "("
    #         and s[i + 1] == ")"
    #         or s[i] == "{"
    #         and s[i + 1] == "}"
    #         or s[i] == "["
    #         and s[i + 1] == "]"
    #     ):
    #         continue
    #     else:
    #         return False
    # return True if len(s) % 2 == 0 else False
    for i in range(len(s)):
        for j in range(i, len(s)):
            if (
                s[i] == "("
                and s[j] == ")"
                or s[i] == "{"
                and s[j] == "}"
                or s[i] == "["
                and s[j] == "]"
            ):
                continue
        else:
            return False

    return True if len(s) % 2 == 0 else False


s = "()[]{}"
print(isvalid(s))
print(list(s))
