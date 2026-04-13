''' given an array prices where prices[i] is the price of a given stock on the ith day.
and want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price=0
        min_price=prices[0]
        for i in range(1,len(prices)):
             max_price=max(max_price,prices[i]-min_price)
             min_price=min(min_price,prices[i])
        return max_price
        
