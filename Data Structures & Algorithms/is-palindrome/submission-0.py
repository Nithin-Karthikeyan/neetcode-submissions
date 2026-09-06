class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def isAlphaNum(c):
            isalpha = (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z'))
            isnum = ord('0') <= ord(c) <= ord('9')
            return (isalpha or isnum)

        while l <= r:
            while l < r and not isAlphaNum(s[l]): # If l is not alphanumeric, then go next index
                l += 1
            while r > l and not isAlphaNum(s[r]):
                r -= 1
            
            # If not alphanum then compare them
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    


        