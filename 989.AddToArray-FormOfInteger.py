class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        s,c=0,0
        l=len(A)
        while l>0 or c>0 or K>0:
            l-=1
            if l<0:
                A.insert(0,0)
                l+=1
            A[l]+=c
            A[l]+=K%10
            c=A[l]//10
            K=K//10
            A[l]=A[l]%10
        return A
            
            
