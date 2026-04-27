class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''.join(filter(str.isalnum, s.lower()))
        n = len(cleaned_s)
        m = n//2

        ls = cleaned_s[:m]
        rs = cleaned_s[(n-m):]
        rrs = rs[::-1]
        return ls == rrs


#Solution 1: Turn all chars to lowers case, remove all non-alphanumeric
# slice string into two substrings of equal sizes
# reverse the right side string, and check if they are equal
# 7 / 2 = 3.5 = 3
# 7 - 3 = 4,5,6