# knapsack
# step 1 : Read number of items n
# step 2 : Read weights array wt[] and values array val[]
# step 3 : Read Knapsacl capacity W
# step 4 : Create DP table dp[n+1][W+1]
# step 5 : Initialize first row and column with 0
# step 6 : for each item i from 1 to n
#          for each weight w from 0 to w
#           if wt [i-1] <= w
#           dp[i][w] = max(
#                  val[i=1] + dp[i-1][w-wt[i-1]],
#                  dp[i-1][w]
#            )
#          else
#           dp[i][w] = dp[i-1][w]
# step 7 : return dp[n][W]          

n = int(input("Enter number of items: "))
wt = list(map(int, input("Enter weights separated by space: ").split()))
val = list(map(int, input("Enter values separated by space: ").split()))
W = int(input("Enter knapsack capacity: "))

dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(W + 1):
        if wt[i - 1] <= w:
            dp[i][w] = max(
                val[i - 1] + dp[i - 1][w - wt[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

print("Maximum value:", dp[n][W])