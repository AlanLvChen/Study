# Problem:
#   Given an integer array nums, find a contiguous non-empty subarray 
#   within the array that has the largest product, and return the product.
#   The test cases are generated so that the answer will fit in a 32-bit integer.
#   A subarray is a contiguous subsequence of the array.



# Example:
#   Input: nums = [2,3,-2,4]
#   Output: 6
#   Explanation: [2,3] has the largest product 6.


def maxProduct(self, nums):
    maxProd = max(nums)
    
    minCur, maxCur = 1, 1
    
    for i in nums:
        
        if i == 0:
            minCur, maxCur = 1,1
            continue
            
            
        temp = maxCur
        maxCur = max(i, maxCur*i, minCur*i)
        minCur = min(i, minCur*i, temp*i)
        
        
        
        if maxCur > maxProd:
            maxProd = maxCur
            
    return maxProd

# O(n) - Time Complexity - Iterate through entire nums
# O(1) - Space Complexity - only saving 3 variables


# Notes:
# Iterate through once. Keep track of minimum and maximum of previous two as you iterate through. 
# The next minimum/max is based on previous