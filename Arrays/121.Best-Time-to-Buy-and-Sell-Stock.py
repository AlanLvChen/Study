# Problem:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a 
# different day in the future to sell that stock. Return the maximum profit you can achieve 
# from this transaction. If you cannot achieve any profit, return 0.


# Example:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

def maxProfit(self, prices):
    
    max_profit = 0                          # O(1)
    cheapest_value = prices[0]              # O(1)
    
    for i in prices:                        # O(n)
        if i < cheapest_value:              # O(1)
            cheapest_value = i
        else:                               # O(1)
            profit = i - cheapest_value
            if profit > max_profit:         # O(1)
                max_profit = profit
    return max_profit
    
# O(n) - Time Complexity - Since it takes O(n) to iterate through prices
# O(1) - Space Complexity - Since we only need two variables to store prices

# Notes:
#
# Iterate once through array. Store cheapest value and store max profit. 
# if current value is less than cheapest day then replace. Otherwise compare profits