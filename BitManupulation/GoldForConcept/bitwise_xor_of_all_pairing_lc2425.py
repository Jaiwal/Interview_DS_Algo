#solution1: brute frorce gives TLE
from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res=0

        for num1 in nums1:
            for num2 in nums2:
                res^=num1^num2

        return res
        
#solution2: saw hint and simply that those who will come odd no of times will come in res

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        m=len(nums2)
        res=0

        #even even
        if m%2==0 and n%2==0:
            return 0

        #even and odd
        if n%2==0 and m%2!=0:
            for num1 in nums1:
                res ^= num1  

        #odd and even
        if n%2!=0 and m%2==0:
            for num2 in nums2:
                res ^= num2 


        #odd and odd
        if n%2!=0 and m%2!=0:
            for num2 in nums2:
                res ^= num2 
            for num1 in nums1:
                res ^= num1  
                
        return res
    

#solution3: can use map also

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        res = 0

        mp = defaultdict(int)

        for num1 in nums1:
            mp[num1]+=m

        for num2 in nums2:
            mp[num2]+=n

        for key, value in mp.items():
            if value % 2 != 0:
                res ^= key

        return res
    

#solution4: improvement of sol2, you dont need to handle all 4 cases but only 2

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0

        if len(nums2) % 2 == 1:  # If nums2 length is odd, XOR all elements in nums1
            for num1 in nums1:
                res ^= num1

        if len(nums1) % 2 == 1:  # If nums1 length is odd, XOR all elements in nums2
            for num2 in nums2:
                res ^= num2

        return res