# Problem:
#   Given an integer array nums, find the contiguous subarray 
#   (containing at least one number) which has the largest sum and return its sum.
#   
#   A subarray is a contiguous part of an array.


# Example:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    maxSub = nums[0]
    curSum = 0
    
    for i in nums:
        if curSum < 0:
            curSum = 0
        curSum += i
        maxSub = max(curSum, maxSub)
    
    return maxSub

    

# O(n) - Time Complexity - Since it takes O(n) to iterate through nums
# O(1) - Space Complexity - Since we are just storing 2 variables

# Notes:
#
# Iterate through once. Two variables for current sum and maxSum. if less than 0, reset curSum. Otherwise max(curSum, maxSum)