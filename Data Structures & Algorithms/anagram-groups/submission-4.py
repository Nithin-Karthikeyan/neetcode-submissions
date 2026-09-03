class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict as dd
        res = dd(list)
        for s in strs:
            count = [0] * 26 # To store the chars in string 's'
            for char in s:
                count[ord(char)-ord('a')] += 1 # Increment the count of that char
            res[tuple(count)].append(s) # Append s to the list with the key as the frequency list
        return list(res.values())