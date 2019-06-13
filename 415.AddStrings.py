class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1,l2=len(num1),len(num2)
        c,s=0,0
        
        out=[]
        while c or l1>0 or l2>0:
            if l1>0:
                l1-=1
                s+=ord(num1[l1])-ord("0")
            if l2>0:
                l2-=1
                s+=ord(num2[l2])-ord("0")
            s+=c
            out.append(chr(s%10+ord("0")))
            c=s//10
            s=0
        return "".join(out[::-1])
