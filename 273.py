# 273. Integer to English Words


def numberToWords(num):
    onces = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
    }
    tens = {
        2: "Twenty",
        3: "Thirty",
        4: "Forty",
        5: "Fifty",
        6: "Sixty",
        7: "Seventy",
        8: "Eighty",
        9: "Ninety",
    }
    if num == 0:
        return "Zero"

    def get_string(n):
        res = []
        hundred = n // 100
        if hundred:
            res.append(onces[hundred] + " Hundred")
        last_2 = n % 100
        if last_2 >= 20:
            tens_place, once_place = last_2 // 10, last_2 % 10
            res.append(tens[tens_place])
            if once_place:
                res.append(onces[once_place])
        elif last_2:
            res.append(onces[last_2])
        return " ".join(res)

    numInWords = []
    postfix = ["", " Thousand", " Million", " billion"]
    i = 0
    while num:
        digits = num % 1000

        res = get_string(digits)
        if res:
            numInWords.append(res + postfix[i])
        num = num // 1000
        i += 1
    numInWords.reverse()
    return " ".join(numInWords)


num = 1000000
print(numberToWords(num))
