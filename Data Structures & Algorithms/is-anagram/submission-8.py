class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ss = sorted(s)
        st = sorted(t)
        for i in range(len(s)):
            if ss[i] != st[i]:
                return False
        return True 
# Solutution 1: Two Hash Sets, If Hash Sets length match, and original strings length match, two hash sets equal -> return true
# Test with Jaar and Jarr -> J,A,R & J,A,R , 4 & 4, 3 & 3 -> can't detect this 

# Solution 2: Sorting both , compare each letter to the next letter -> will work but slow

# Soltuion 3: Use hash table (dicts) -> [Letter -> Count], two hash tables, compare each key and each value
# {
#             if len(s) != len(t):
#             return False
#         dict_s = {}
#         dict_t = {}
#         for i in range(len(s)):
#             if s[i] in dict_s:
#                 dict_s[s[i]] += 1
#             else:
#                 dict_s[s[i]] = 1
#             if t[i] in dict_t:
#                 dict_t[t[i]] += 1
#             else:
#                 dict_t[t[i]] = 1
#         return dict_s == dict_t
# }