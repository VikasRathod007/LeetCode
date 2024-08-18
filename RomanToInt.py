def roman(s):
    # I=1
    # V=5
    # X=10
    # L=50
    # C=100
    # D=500
    # M=1000
    # IV=4
    # IX=9
    # XL=40
    # XC=90
    # CD=400
    # CM=900
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    pre_val = 0
    for char in reversed(s):
        val = roman_dict[char]
        if val < pre_val:
            total -= val
        else:
            total += val
            pre_val = val
    return total


s = "IV"
print(roman(s))
