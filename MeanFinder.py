def mean(D, M):
    # Mean_M = 0
    # for i in range(3):
    #     Mean_M += M
    # D = Mean_M + D
    # return D // 4
    return (3 * M + D) // 4


D = 13
M = 9
print(mean(D, M))
