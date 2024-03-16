class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 :
            return False
        y=x
        z=0
        while y>0:
            i=y%10
            z=z*10+i
            y//=10
        if z==x:
            return True
        else:
            return False
