class Solution(object):
    def maxArea(self, h):
        a = l=0
        x= len(h) - 1
        while l<x:
            b= (x-l) * min(h[x],h[l])
            a=max(a,b)
            if h[l]<h[x]:
                l+=1
            else:
                x-=1
        return a