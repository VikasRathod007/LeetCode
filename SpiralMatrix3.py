def spiralMatrixIII(rows, cols, rStart, cstart):

    res = []
    r, c = rStart, cstart
    direction = 0
    steps = 1
    while len(res) < rows * cols:
        for i in range(2):
            for i in range(steps):
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
                if direction == 0:
                    c += 1
                elif direction == 1:
                    r += 1
                elif direction == 2:
                    c -= 1
                elif direction == 3:
                    r -= 1
            direction = (direction + 1) % 4

        steps += 1
    return res


rows = 1
cols = 4
rStart = 0
cStart = 0
print(spiralMatrixIII(rows, cols, rStart, cStart))
