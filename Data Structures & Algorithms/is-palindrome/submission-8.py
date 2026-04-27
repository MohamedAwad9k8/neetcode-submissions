class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''.join(filter(str.isalnum, s.lower()))
        l, r = 0, len(cleaned_s)-1
        while l < r:
            if cleaned_s[l] != cleaned_s[r]:
                return False
            l += 1
            r -= 1
        return True

#Solution 1: Turn all chars to lowers case, remove all non-alphanumeric
# slice string into two substrings of equal sizes
# reverse the right side string, and check if they are equal
# 7 / 2 = 3.5 = 3
# 7 - 3 = 4,5,6

#Solution 2 : two pointers