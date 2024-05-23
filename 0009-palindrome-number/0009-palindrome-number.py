class Solution(object):
    def isPalindrome(self, x):
        a= str(x)[::-1]
        try:
            i = int(a)
            return i == x
        except ValueError:
            return False