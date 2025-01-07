from typing import List

#solution1: nearly n3 solution
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]

        for word in words:
            for anotherword in words:
                if anotherword!=word:
                    if word in anotherword:
                        if word not in res:
                            res.append(word)

        return res
        
#solution2: using KMP and trie, yet to cover
