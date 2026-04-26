class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {} # num : count in array
        top_freq_nums = []
        uniques = set(nums)

        for unique in uniques:
            num_dict[unique] = nums.count(unique)

        for i in range (k):
            max_val = 0
            for k,v in num_dict.items():
                if v >= max_val:
                    max_val = v
                    top_frq_num = k
            
            top_freq_nums.append(top_frq_num)
            num_dict.pop(top_frq_num, None)
        return top_freq_nums
