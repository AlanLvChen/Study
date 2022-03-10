# Problem:
#   Given an array of integers nums and an integer target, return indices 
#   of the two numbers such that they add up to target. You may assume that 
#   each input would have exactly one solution, and you may not use the same element twice.

#   You can return the answer in any order.
#   and return false if every element is distinct.


# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]


def twoSum(self, nums, target):
    
    hashmap = dict()                        # O(1)
    
    for i, val in enumerate(nums):          # O(n)
        value = target - val
    
        if value in hashmap:                # O(1)
            return [hashmap[value], i]
        
        hashmap[val] = i                    # O(1)
    

# O(n) - Time Complexity - Since it takes O(n) to iterate through nums
# O(n) - Space Complexity - Since worst case is we add entire nums O(n) to the set

# Notes:
#
# Iterate once through array and check Hashmap for the value needed. Hashmap allows for O(1) look up time.