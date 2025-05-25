from collections import defaultdict
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        mp=defaultdict(int)
        res=0

        for word in words:
            reverseword=word[::-1]
            if reverseword in mp and mp[reverseword] > 0:
                res+=4
                mp[reverseword] -= 1
            else:
                mp[word]+=1

        for key,value in mp.items():
            if key==key[::-1] and value>0:
                res+=2
                break

        return res

"""
Use map

1. when diff char word then find reverse in map and increment res by 4 and dec the count in map
2. after that you can only take up same char word only once therefore iterate again
"""