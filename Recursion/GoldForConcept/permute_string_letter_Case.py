from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        temp=[]
        i=0
        self.printallpermutations(nums,i,temp,res)

        return res

    def printallpermutations(self,nums,index,temp,res):
        if index>=len(nums):
            res.append(''.join(temp[:]))
            return

        #take lower than call further
        temp.append(nums[index].lower())
        self.printallpermutations(nums,index+1,temp,res)
        temp.pop()
        #undo what you do did

        #take upper case of current char than call further
        temp.append(nums[index].upper())
        self.printallpermutations(nums,index+1,temp,res)
        temp.pop()
    

if __name__ == "__main__":
    sol = Solution()
    input_str = "ab"
    output = sol.permute(input_str)
    print("Output permutations:")
    for o in output:
        print(o)