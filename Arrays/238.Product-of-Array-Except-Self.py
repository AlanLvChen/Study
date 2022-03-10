# Problem: Given an integer array nums, return an array answer 
#   such that answer[i] is equal to the product of all the elements 
#   of nums except nums[i]. The product of any prefix or suffix of 
#   nums is guaranteed to fit in a 32-bit integer. 
# 
#   You must write an algorithm 
#   that runs in O(n) time and without using the division operation.


# Example: 
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]


def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    output = []
    
    p = 1
    for i in range(len(nums)):
        output.append(p)
        p = p * nums[i]
        
        
    p = 1
    for i in range(len(nums)-1, -1, -1):
        output[i] = output[i] * p
        p = p * nums[i]
    
    return output


# O(n) - Time Complexity - Iterating through nums twice
# O(1) - Space Complexity - Since answer array does not count it is O(1) 

# Notes:
#
# Iterate and store everthing multiplied left of the current value. 
# Use a pointer with value 1 to start. Append first then change p. Apply again with right to left