class Solution(object):
    def reverseNum(self, x):
        sum=0
        while (x!=0):
            digit = x%10
            sum=sum*10+digit
            x//=10
        return sum
    def limit(self, a):
        if a<2**31 - 1 and a>-2**31:
            return a
        else:
            return 0
    
    def reverse(self, x):
        if x>=0 :
            b = self.reverseNum(x)
            return self.limit(b)
        elif x<0 :
            a=abs(x)
            a=self.reverseNum(a)
            a*=-1
            return self.limit(a)