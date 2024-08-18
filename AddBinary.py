def addBinary(a, b):
    return bin(int(a, 2) + int(b, 2)).replace("0b", "")


a = "11"
b = "1"
print(addBinary(a, b))
print(int(a, 2) + int(b, 2))
