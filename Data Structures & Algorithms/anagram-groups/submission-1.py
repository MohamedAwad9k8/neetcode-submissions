class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for string in strs:
            char_count = [0] * 26

            for char in string:
                char_count[ord(char) - ord("a")] += 1
            
            key = tuple(char_count)
            if not key in result:
                result[key] = []
            result[key].append(string)
        return list(result.values())
        