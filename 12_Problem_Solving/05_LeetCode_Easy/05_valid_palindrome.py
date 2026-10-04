class Solution:
    def isPalindrome(self, s):

        cleaned = ""

        for char in s:

            if char.isalnum():
                cleaned += char.lower()

        return cleaned == cleaned[::-1]


# Example
solution = Solution()

s = "A man, a plan, a canal: Panama"

print(solution.isPalindrome(s))