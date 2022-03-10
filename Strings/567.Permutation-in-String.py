# Problem
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.


# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").


#IDEA: Sliding Window will keep the time complexity to O(s1 + s2)
def containsPermutation(s1, s2):
    
    

# INITIAL idea:
# While this works, think of the runtime. 
# O(s1 + s2^2) - Time complexity
# def containsPermutation(s1, s2):

#     charArray = [0] * 26                                  O(1)

#     undo = []                                             O(1)

#     for i in s1:                                          O(s1)
#         val = ord('a') - ord(i)                           O(1)
#         charArray[val] += 1                               O(1)

#     for i in range(len(s2)):                              O(s2)
#         val = ord('a') - ord(s2[i])                       O(1)

#         ptr = i                                           O(1)

#         while charArray[val] > 0 and ptr < len(s2):       O(s1)
#             undo.append(val)                              O(1)
#             charArray[val] -= 1                           O(1)
#             ptr += 1                                      O(1)
#             val = ord('a') - ord(ptr)                     O(1)
        
#         if sum(charArray) == 0:                           O(1)
#             return True                                   O(1)
#         else:
#             for i in undo:                                O(s1)
#                 charArray[i] += 1                         O(1)

#     return False                                          O(1)
        
        