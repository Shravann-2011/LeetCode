class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)
        
        # 2. Base case: 0 coins are needed to make an amount of 0
        dp[0] = 0
        
        # 3. Build up solutions for every sub-amount from 1 to amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    # Take the minimum between keeping current value
                    # or adding 1 coin and looking up the remaining balance
                    dp[i] = min(dp[i], 1 + dp[i - coin])
                    
        # 4. If dp[amount] is still infinity, it's impossible to make that amount
        return dp[amount] if dp[amount] != amount + 1 else -1