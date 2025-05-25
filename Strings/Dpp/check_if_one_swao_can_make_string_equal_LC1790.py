#brute

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff=0
        n=len(s1)
        mp1=[0 for _ in range(26)]
        mp2=[0 for _ in range(26)]

        for i in range(n):
            if s1[i]!=s2[i]:
                diff+=1
                if diff>2:
                    return False
            mp1[ord(s1[i])-ord('a')]+=1
            mp2[ord(s2[i])-ord('a')]+=1
                

        for i in range(26):
            if mp1[i]!=mp2[i]:
                return False

        return True

#optimal

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff=0
        n=len(s1)
        firstIn=-1
        secondIn=-1

        for i in range(n):
            if s1[i]!=s2[i]:
                diff+=1
                if diff>2:
                    return False
                elif diff==1:
                    firstIn=i
                else:
                    secondIn=i

        return s1[firstIn]==s2[secondIn] and s1[secondIn]==s2[firstIn]


                    


                

        for i in range(26):
            if mp1[i]!=mp2[i]:
                return False

        return True

        