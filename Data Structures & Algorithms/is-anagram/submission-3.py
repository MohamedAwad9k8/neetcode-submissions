class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not (len(s) == len(t)):
                return False
        occurences = {}
        for letter in s:
            if letter in occurences:
                occurences[letter] += 1
            else:
                occurences[letter] = 1

        for key in occurences:
            if not (t.count(key) == occurences[key]):
                return False
        return True