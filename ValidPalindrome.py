def IsPalindrome(Sentence):
    if Sentence == " ":
        return True
    OnlyAlpha = [char for char in Sentence if char.isalpha()]
    OnlyAlpha = "".join(OnlyAlpha).lower
    print(OnlyAlpha)
    return OnlyAlpha == OnlyAlpha[::-1]


s = "A man, a plan, a canal: Panama"
s1 = " "
print(IsPalindrome(s))
