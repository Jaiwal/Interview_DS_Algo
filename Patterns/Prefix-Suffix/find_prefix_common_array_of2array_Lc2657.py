from typing import List
#solution1 : just check at i from 0 to i what element if that element is present in other
#n3 solution

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)

        res=[0 for _ in range(n)]
        

        for i in range(n):
            count=0
            for j in range(i+1):
                for m in range(i+1):
                    if A[j]==B[m]:
                        count+=1

            res[i]=count

        return res
    
#solution2: have a list that track what element seen so far and iterate in that list for every i as how many are true so far

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)

        isPresentA=[False for  _ in range(n+1)]
        isPresentB=[False for _ in range(n+1)]
        res=[0 for _ in range(n)]


        for i in range(n):
            isPresentA[A[i]]=True
            isPresentB[B[i]]=True

            count=0

            #check how many true so far(ith)
            for k in range(1,n+1):
                if isPresentA[k] and isPresentB[k]:
                    count+=1

            res[i]=count

        return res
    

#solution3: keep map and traverse in list incrementing found value and since every value will occur only once, you will have each value occured as twice so check if count is 2 then increment count found so far


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)

        count=0
        res=[0 for _ in range(n)]
        mp={}


        for i in range(n):

            if A[i] not in mp:
                mp[A[i]]=1
            else:
                mp[A[i]]+=1

            if mp[A[i]]==2:
                count+=1
            
            if B[i] not in mp:
                mp[B[i]]=1
            else:
                mp[B[i]]+=1

            if mp[B[i]]==2:
                count+=1

            res[i]=count

        return res


            

           




        