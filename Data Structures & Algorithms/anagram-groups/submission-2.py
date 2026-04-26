class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for string in strs:
            key = tuple(sorted(string))
            if not key in result:
                result[key] = []
            result[key].append(string)
        return list(result.values())