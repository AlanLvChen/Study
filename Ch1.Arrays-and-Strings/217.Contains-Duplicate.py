# Problem:
#   Given an integer array nums, return true if any value appears at least twice in the array, 
#   and return false if every element is distinct.


# Example:
# Input: nums = [1,2,3,4]
# Output: false


def hasDuplicate(nums):

    check = set()               # O(1)

    for i in nums:              # O(n)
        if i in check:          # O(1)
            return True         # O(1)
        
        check.add(i)            # O(1)
    
    return False                # O(1)


# O(n) - Time Complexity - Since it takes O(n) to iterate through nums
# O(n) - Space Complexity - Since worst case is we add entire nums O(n) to the set