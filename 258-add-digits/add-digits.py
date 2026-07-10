class Solution(object):
    def addDigits(self, num):
        while num>=10:
            sum=0
            while num>0:
                digit=num%10
                sum+=digit
                num//=10
            num=sum
        return num
    
        