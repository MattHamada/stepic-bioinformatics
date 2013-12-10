def DPChange(money, coins):
    minNumCoins = [0]
    for m in range(1,money+1):
        minNumCoins.append(1000)
        for i in range(0, len(coins)):
            if m >= coins[i]:
                if minNumCoins[m-coins[i]] + 1 < minNumCoins[m]:
                    minNumCoins[m] = minNumCoins[m-coins[i] ]+1
    return minNumCoins[-1]

print DPChange(18697, [81, 9, 5, 3, 1])
