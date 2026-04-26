class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g_anagrams = []
        sublist = []
        strs_dicts = []
        seen_anagrams = set()
        for string in strs:
            strs_dicts.append({"string" : "".join(sorted(string)), "length" : len(string)} )
        
        for i in range(len(strs)):
            # Skip Anagrams that had already been recorded
            if strs_dicts[i]["string"] in seen_anagrams:
                continue
            for j in range(i+1, len(strs)):
                if (strs_dicts[i] == strs_dicts[j]):
                    # Handle First occurence of Anagram
                    if len(sublist) == 0:
                        sublist.append(strs[i])
                    # Handle all consecutive occurences of Anagram    
                    sublist.append(strs[j])
            # Handle lonely strings
            if not sublist:
                sublist.append(strs[i])
            g_anagrams.append(sublist)
            # Update Hash Set with Seen Anagrams 
            seen_anagrams.add(strs_dicts[i]["string"])
            # Initialize a new Sublist
            sublist = []
        return g_anagrams

        