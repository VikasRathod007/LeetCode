# 205. Isomorphic Strings


def Isomorphic(s, t):
    straight = {}
    reverse = {}
    for i in range(len(s)):
        c1, c2 = s[i], t[i]
        if (c1 in straight and straight[c1] != c2) or (
            c2 in reverse and reverse[c2] != c1
        ):
            return False
        straight[c1] = c2
        reverse[c2] = c1
    return True


s = "egg"
t = "add"
print(Isomorphic(s, t))
