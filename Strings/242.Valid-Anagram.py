# Problem:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

 

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true


def isAnagram(s, t):

    if len(s) != len(t):            # O(1)
        return False

    charArray = [0]*26              # O(1)

    for i in s:                     # O(s)
        val = ord('a') - ord(i)     
        charArray[val] += 1

    for i in t:                     # O(s)
        val = ord('a') - ord(i)
        if charArray[val] < 1:
            return False
        charArray[val] -= 1
    

    if sum(charArray) > 0:          # O(s)
        return False
    return True


# 