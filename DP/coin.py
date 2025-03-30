coins=[2,3,5]
amount=1000

# dp=[0]*(amount+1)
# dp[0]=1

# for coin in coins:
#     for i in range(coin,amount+1):
#         dp[i] = dp[i] + dp[i-coin]
#     print(dp)
        
        
# print(dp[-1])
result = 0
for i in range(len(coins)-1, -1,-1):
    curr_coins = amount//coins[i]
    result += curr_coins
    if amount == 0:
        break
    amount -= coins[i]*curr_coins
    
    
    
if amount == 0:
    print(result)
else:
    print("no denominations")
    

    
    
    

    
    
    



