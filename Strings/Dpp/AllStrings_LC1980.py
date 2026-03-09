from typing import List
class Solution:
    def permute(self, n: int) -> List[List[int]]:
        res=[]
        i=0
        self.printallpermutations(n,i,"",res)

        return res

    def printallpermutations(self,n,index,temp,res):
        if index>=n:
            res.append(temp)
            return

        

        self.printallpermutations(n,index+1,temp+'0',res)
       

       
    
        self.printallpermutations(n,index+1,temp+'1',res)
  
    

if __name__ == "__main__":
    sol = Solution()
    n = 3
    output = sol.permute(n)
    print("Output permutations:")
    for o in output:
        print(o)