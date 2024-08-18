def lengthOfLastWord(s):
    s = "".join(s).split()
    print(len(s[len(s) - 1]))


s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))
