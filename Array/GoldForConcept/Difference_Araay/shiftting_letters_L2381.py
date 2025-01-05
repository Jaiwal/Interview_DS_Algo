#solution1: brute force, just process every query

#solution 2: use difference array

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        diff=[0]*n

        for query in shifts:
            l=query[0]
            r=query[1]
            u=query[2]

            if u==0:
                x=-1
            else:
                x=+1
            
            #process every shift query
            diff[l]+=x
            if r+1<n:
                diff[r+1]-=x
            
        #find resultant shift needed in diff
        for i in range(1,n):
            diff[i]+=diff[i-1]
        s=list(s)
        #modify string
        for i in range(n):
            value=ord(s[i])-ord('a')
            total_shift=(value+diff[i])%26 #wrap around
            if total_shift<0:
                total_shift+=26 #circular wrap around
            
            s[i]=chr(total_shift+ord('a'))
            

        return ''.join(s)
                


            



        