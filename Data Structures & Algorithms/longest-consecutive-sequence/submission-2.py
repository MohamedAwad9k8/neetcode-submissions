class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique_elements = sorted(set(nums))

        max_seq = 1
        curr_seq = 1

        for i in range(1, len(unique_elements)):
            if unique_elements[i] == unique_elements[i - 1] + 1:
                curr_seq += 1
            else:
                max_seq = max(max_seq, curr_seq)
                curr_seq = 1

        # Final update for ending streak
        return max(max_seq, curr_seq)