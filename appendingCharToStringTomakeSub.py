def appendCharacters(s, t):
    j = 0
    for char in s:
        if char == t[j]:
            j += 1
    return len(t) - j


s = "abcde"
t = "z"
appendCharacters(s, t)
print(appendCharacters(s, t))  # Output: 4
