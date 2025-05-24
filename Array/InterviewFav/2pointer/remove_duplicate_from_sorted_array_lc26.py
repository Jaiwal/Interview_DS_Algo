
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0 #will always point to unique element 
        j=1 #will explore and find unique element to give to i

        while j<n:
            if nums[j]!=nums[i]:
                #found unique element, i will make space now
                i+=1
                nums[i]=nums[j]
            j+=1
        
        return i+1
        