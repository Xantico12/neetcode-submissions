class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        currentProfit = 0
        maxProfit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r = l + 1
            else:
                currentProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit, currentProfit)
                r += 1
                
        return maxProfit

