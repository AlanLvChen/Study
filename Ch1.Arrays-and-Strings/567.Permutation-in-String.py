# Problem
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.


# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").


def containsPermutation(s1, s2):

    charArray = [0] * 26

    undo = []

    for i in s1:
        val = ord('a') - ord(i)
        charArray[val] += 1

    for i in range(len(s2)):
        val = ord('a') - ord(s2[i])

        ptr = i

        while charArray[val] > 0 and ptr < len(s2):
            undo.append(val)
            charArray[val] -= 1
            ptr += 1
            val = ord('a') - ord(ptr)
        
        if sum(charArray) == 0:
            return True
        else:
            for i in undo:
                charArray[i] += 1

    return False    
        
        