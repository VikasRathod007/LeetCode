def dailyTemperatures(Temp):
    res = []
    for i in range(0, len(Temp) - 1):
        for j in range(i + 1, len(Temp)):
            if Temp[j] > Temp[i]:
                res.append(j - i)
                break
        else:
            res.append(0)
    res.append(0)
    return res


temperatures = [30, 38, 30, 36, 35, 40, 28]
print(dailyTemperatures(temperatures))
