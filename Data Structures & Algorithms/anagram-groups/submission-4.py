from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            res_dict[key].append(word)
        return list(res_dict.values()) 

# solution 1: turn each string into a tuple, sort it, use tuple as key for dict
# the value of each key should be an array of indices
# return a list of sublists, where each sublist is the value of a key, but mapped from indices to values