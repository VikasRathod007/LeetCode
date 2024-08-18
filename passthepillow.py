def passThePillow(n, time):
    arr = [i for i in range(1, n + 1)]
    i = 0
    while time > 0:
        while time > 0 and i < len(arr) - 1:
            time -= 1
            i += 1
        while time > 0 and i > 0:
            time -= 1
            i -= 1
    return arr[i]


n = 4
time = 5
print(passThePillow(n, time))
