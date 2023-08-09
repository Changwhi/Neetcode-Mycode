class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        res = 0
        for number in prices:
            res = max((number-minPrice), res)
            minPrice = min(number, minPrice)
        return res
