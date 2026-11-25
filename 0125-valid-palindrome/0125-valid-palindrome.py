class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j :
            right = s[j]
            left = s[i]

            if not right.isalnum():
                j = j - 1
                continue
            if not left.isalnum():
                i = i + 1
                continue

            if left.lower() != right.lower():
                return False
            
            i = i + 1
            j = j - 1
        return True