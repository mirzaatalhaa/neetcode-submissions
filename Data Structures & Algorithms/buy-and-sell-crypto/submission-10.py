class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        max_profit = 0 
        current_profit = 0 

        while r < len(prices):
            if prices[l] > prices[r]:
                l=r 
                r+=1
            else:
                current_profit = prices[r] - prices[l]
                r+=1
                max_profit = max(max_profit, current_profit) 
                    
        return max_profit


        
        