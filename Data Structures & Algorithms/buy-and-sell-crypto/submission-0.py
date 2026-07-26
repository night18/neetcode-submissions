class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        profit = 0

        curr_low = prices[0]

        for i in range(1, len(prices)):
            profit = max(prices[i] - curr_low, profit)
            curr_low = min(prices[i], curr_low) 


        return profit