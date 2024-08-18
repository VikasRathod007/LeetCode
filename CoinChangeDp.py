def change(coins, n):
    # coins.sort()
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = float("inf")
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    print(dp)
    return dp[n] if dp[n] != float("inf") else -1


coins = [1, 3, 4]
n = 34
print(change(coins, n))
