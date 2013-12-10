minCoins = [0,1,2,3,4,1,1,2,3,4,2,2,2]
total = [0,1,2,3,4,5,6,7,8,9,10,11,12]
coins = [1,5,6]

for i in range(13,23):
    a = minCoins[i-coins[0]]
    b = minCoins[i-coins[1]]
    c = minCoins[i-coins[2]]
   # print i, a, b, c
    smallest = min(a,b,c)+1
    minCoins.append(smallest)
    print smallest
    total.append(i)



