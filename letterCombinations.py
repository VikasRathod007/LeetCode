def letterCombinations(digits):
    # comb = [2, 3, 4, 5, 6, 7, 8, 9]
    # letters = [
    #     ["a", "b", "c"],
    #     ["d", "e", "f"],
    #     ["g", "h", "i"],
    #     ["j", "k", "l"],
    #     ["m", "n", "o"],
    #     ["p", "q", "r", "s"],
    #     ["t", "u", "v"],
    #     ["w", "x", "y", "z"],
    # ]
    # comb = [
    #     [2, ["a", "b", "c"]],
    #     [3, ["d", "e", "f"]],
    #     [4, ["g", "h", "i"]],
    #     [5, ["j", "k", "l"]],
    #     [6, ["m", "n", "o"]],
    #     [7, ["p", "q", "r", "s"]],
    #     [8, ["t", "u", "v"]],
    #     [9, ["w", "x", "y", "z"]],
    # ]
    comb = {
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"],
    }
    res = []
    x = list(digits)


digits = "23"
print(letterCombinations(digits))
