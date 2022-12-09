## https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        n = len(x)
        mid = n//2
        # print(x,n,mid, x[mid:])
        if n % 2 == 0:
            return x[:mid] == x[mid::][::-1]
        else:
            return x[:mid] == x[mid+1:][::-1]
