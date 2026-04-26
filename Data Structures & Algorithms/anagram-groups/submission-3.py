class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = {}
        for i, word, in enumerate(strs):
            temp_t = tuple(sorted(tuple(word)))
            if temp_t in res_dict:
                res_dict[temp_t].append(i)
            else: 
                res_dict[temp_t] = [i]
        res_list = []
        for value in res_dict.values():
            sub_list = []
            for indx in value:
                sub_list.append(strs[indx])
            res_list.append(sub_list)
        return res_list

# solution 1: turn each string into a tuple, sort it, use tuple as key for dict
# the value of each key should be an array of indices
# return a list of sublists, where each sublist is the value of a key, but mapped from indices to values