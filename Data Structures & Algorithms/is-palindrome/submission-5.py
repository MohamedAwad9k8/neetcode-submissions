class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum())
        s = s.lower()
        n = len(s)
        m = n // 2

        l1 = 0
        l2 = m
        r1 = m if (n%2) == 0 else m+1 #if odd str, skip middle char
        r2 = n


        s1 = s[l1:l2]
        s2 = s[r1:r2]
        s2 = s2[::-1]

        if s1 == s2:
            return True
        else:
            return False
