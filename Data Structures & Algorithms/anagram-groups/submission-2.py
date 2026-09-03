class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict as dd
        # Sort the strings, and do a O(n2) loop and use that index in the original list to append to new list - Way too inefficient

        # strs_sorted = []
        # res = []

        # if len(strs) == 1:
        #     return [[strs[0]]]
        # if len(strs) == 0:
        #     return [[]]
        # for string in strs:
        #     strs_sorted.append(sorted(string))
        
        # for i, str1 in enumerate(strs_sorted):
        #     anagram_i = []
        #     for j, str2 in enumerate(strs_sorted):
        #         if str1 == str2:
        #             anagram_i.append(strs[j])
        #     # print(anagram_i)
        #     if anagram_i not in res:
        #         res.append(anagram_i)
        #     # print(res)
        # return res

        # Use defaultdict and frequency of chars as the key
        res = dd(list)

        for s in strs:
            count = [0] * 26 # To store the chars in string 's'
            for char in s:
                count[ord(char)-ord('a')] += 1 # Increment the count of that char
            res[tuple(count)].append(s) # Append s to the list with the key as the frequency list
        return list(res.values())