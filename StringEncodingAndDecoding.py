def Encoding(string):
    encoded_string = ""

    for i in string:
        encoded_string += i + "`"
    return encoded_string


def Decoding(encoded_string):
    x = encoded_string.split("`")
    if x[-1] == "":
        x = x[:-1]
    return x


list_of_string = ["we", "say", ":", "yes", "!@#$%^&*()"]

encoded = Encoding(list_of_string)
print(encoded)
print(Decoding(encoded))
