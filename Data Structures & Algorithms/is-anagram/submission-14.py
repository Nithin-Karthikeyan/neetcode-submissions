class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for x in s:
            count[x] = count.get(x, 0) + 1

        for y in t:
            if y not in count.keys() or count[y] == 0:
                return False
            count[y] -= 1   
        
        return True
