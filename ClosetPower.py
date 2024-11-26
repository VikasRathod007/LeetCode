def nearest_power(A, B):
    closest_X = None
    smallest_difference = float("inf")
    p = 0

    while True:
        X = A**p

        difference = abs(X - B)

        if difference < smallest_difference:
            closest_X = X
            smallest_difference = difference
        else:
            break

        if X > B and A > 1:
            break

        p += 1

    return closest_X


A = 2
B = 8
print(nearest_power(A, B))
