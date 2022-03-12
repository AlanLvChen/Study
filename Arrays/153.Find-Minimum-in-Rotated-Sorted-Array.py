# Problem:
#   Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
#   For example, the array nums = [0,1,2,4,5,6,7] might become:
#
#   [4,5,6,7,0,1,2] if it was rotated 4 times.
#   [0,1,2,4,5,6,7] if it was rotated 7 times.
#
#   Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time 
#   results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#   Given the sorted rotated array nums of unique elements, return the minimum element of this array.
#   You must write an algorithm that runs in O(log n) time.



# Example:
#   Input: nums = [3,4,5,1,2]
#   Output: 1
#   Explanation: The original array was [1,2,3,4,5] rotated 3 times.


def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    r = len(nums) - 1
    l = 0
    
    while l < r:
        
        m = (l+r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    return nums[l]

# O(log n) - Time Complexity - Because we are dividing the area we are searching by half every time
# O(1) - Space Complexity - Using pointers


# Notes:
#
# Use Binary Tree. while left < right. If middle is greater than right then search mid --> right. Else search left --> mid
