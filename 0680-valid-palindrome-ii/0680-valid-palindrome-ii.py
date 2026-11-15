class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        def palindrome_helper(i,j,s):
            while i < j:
                if(s[i] != s[j]):
                    return False

                i = i + 1
                j = j - 1
            return True

        while i < j:
            if(s[i] != s[j]):
                return palindrome_helper(i+1, j,s) or palindrome_helper(i, j-1,s)

            else:
                i = i + 1
                j = j - 1
        
        return True