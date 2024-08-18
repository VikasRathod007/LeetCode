def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


def fiboseries(n):
    series = []
    for i in range(0, n + 1):
        series.append(fibo(i))
    return series


# print(fiboseries(10))
def Fibonacci(n):
    series = [0, 1]

    for i in range(2, n + 1):
        series.append(series[i - 1] + series[i - 2])
        print(i)
    return series


# print(Fibonacci(10))


# GCD
def EuclideGCD(a, b):
    if b == 0:
        return a
    else:
        return EuclideGCD(b, a % b)


print(EuclideGCD(357, 234))
