class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        currentProfit = 0
        maxProfit = 0

        while j < len(prices):
            if prices[i] > prices[j]:
                i = j
                j = i + 1
            else:
                currentProfit = prices[j] - prices[i]
                maxProfit = max(maxProfit, currentProfit)
                j += 1
                
        return maxProfit

