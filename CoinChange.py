def coinChange(coins, amount):
    ans = 0
    coins.sort()
    if amount == 0:
        return 0
    for i in reversed(coins):
        if amount // i > 0:
            ans += amount // i
            amount = amount % i
    print(ans, amount)
    return ans if amount == 0 else -1


coins = [186, 419, 83, 408]
amount = 6249
print(coinChange(coins, amount))
