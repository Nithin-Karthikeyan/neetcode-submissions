class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_dict_s = {x: 0 for x in s} # Doesnt matter if x is duplicated
        freq_dict_t = {y: 0 for y in t}
        if sorted(list(freq_dict_s.keys())) != sorted(list(freq_dict_t.keys())):
            return False

        for x in s:
            freq_dict_s[x] += 1 # Increment number of times x appears in the word
        for y in t:
            freq_dict_t[y] += 1
        
        for i in list(freq_dict_s.keys()):
            if freq_dict_s[i] != freq_dict_t[i]:
                return False
        
        return True