class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict={}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        sorted_items = sorted(freq_dict.items(), key = lambda x : x[1], reverse = True)
        return [item[0] for item in sorted_items[:k]]
        

# Solution 1: Dict to save key=num -> value=frequency
# enumerate key, value from dict, sort by value desc, append and pop for K times

# Solution 2: Dict to save key=num -> value=frequency
# return list of keys, in for loop range k, k-1 on each step, pick max number
# identify it's index, get key for index on key list, add it to result_list
# set value to 0 in value array, so it's not chosen as max again