class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # THis is not hitting 100% runtime since ord is python interpreter overhead
        # from collections import defaultdict as dd
        # res = dd(list)
        # for s in strs:
        #     count = [0] * 26 # To store the chars in string 's'
        #     for char in s:
        #         count[ord(char)-ord('a')] += 1 # Increment the count of that char
        #     res[tuple(count)].append(s) # Append s to the list with the key as the frequency list
        # return list(res.values())

        # Using C-based string sorting methods to make it faster
        from collections import defaultdict as dd
        res = dd(list)
        for s in strs:
            res["".join(sorted(s))].append(s)
        return list(res.values())
        