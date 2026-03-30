class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while not self.isAlphaNum(s[left]) and left < right:
                print(s[left])
                left += 1
            while not self.isAlphaNum(s[right])  and left < right:
                print(s[right])
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
        return True
            
        
    def isAlphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))