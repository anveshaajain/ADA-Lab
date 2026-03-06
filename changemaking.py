# algorithm 
#step 1: Start
#step 2: Input the list of coin denominations coins and the target amount
#step 3: Create a DP array dp of size amount + 1
#step 4: Initialize all values of dp with infinity (∞) because we assume the amount cannot be formed initially
#step 5: Set dp[0] = 0 because 0 coins are needed to make amount 0
#step 6: For every amount i from 1 to amount:
#        *For each coin in coins:
#        *If coin ≤ i, then update:
#        *dp[i] = min(dp[i], dp[i - coin] + 1)
#         This checks whether using the current coin reduces the number of coins needed
#step 7: After filling the DP array:
#        *If dp[amount] is still ∞, return -1 (amount cannot be formed)
#         Otherwise return dp[amount]
#step 8: End 


def coin_change_min(coins, amount):
    # Create DP array
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed to make amount 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


# Example
coins = [1, 2, 4, 5]
amount = 4
print("Minimum coins required:", coin_change_min(coins, amount))

