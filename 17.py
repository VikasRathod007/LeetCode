# 17. Letter Combinations of a Phone Number
def letterCombinations(digits):
    mapping_ = {
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"],
    }
    if not digits:
        return []
    each_digit = list(map(int, digits))
    # print(each_digit)
    comb = [""]
    for i in each_digit:
        s = mapping_[i]
        comb = [a + b for a in comb for b in s]
    return comb


digits = "23"
print(letterCombinations(digits))
