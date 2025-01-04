
#solution 1: extreme brute force by detecting pattern
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        mp = set()
        self.count3PS(s, mp, 3, 0, '')
        return len(mp)

    def count3PS(self, string, mp, length, index, currentSub):
        if len(currentSub) == length and self.isPalindrome(currentSub):
            mp.add(currentSub)
            return

        if index == len(string):
            return
        
        # Include
        self.count3PS(string, mp, length, index + 1, currentSub + string[index])

        # Exclude
        self.count3PS(string, mp, length, index + 1, currentSub)

    def isPalindrome(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True

        # Check all substrings of length 2 and above
        for length in range(2, n + 1):  # Length of the substring
            for i in range(n - length + 1):
                j = i + length - 1  # Endpoint of the substring
                
                if s[i] == s[j]:  # Characters at the ends must match
                    if length == 2:  # Substring of length 2 is a palindrome if both characters match
                        dp[i][j] = True
                    else:  # For longer substrings, check the inner substring
                        dp[i][j] = dp[i + 1][j - 1]

        # Check if the entire string is a palindrome
        return dp[0][n - 1]
    

#solution2: dont really need dp func since 3 length palindrome need to check

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        mp = set()
        self.count3PS(s, mp, 3, 0, '')
        return len(mp)

    def count3PS(self, string, mp, length, index, currentSub):
        if len(currentSub) == length and currentSub[0] == currentSub[-1]:
            mp.add(currentSub)
            return

        if index == len(string):
            return
        
        # Include
        self.count3PS(string, mp, length, index + 1, currentSub + string[index])

        # Exclude
        self.count3PS(string, mp, length, index + 1, currentSub)

 
 #solution3: both above gives TLE because ofc 3 <= s.length <= 105

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        mp=set()
        n=len(s)

        for i in range(n):
            mp.add(s[i])
        res=0
        for char in mp:
            first_index=-1
            last_index=-1

            for i in range(n):
                if s[i]==char:
                    if first_index==-1:
                        first_index=i
                    last_index=i
            #we now have all the palindrome for current char, now take only unique ones
            charerc=set()

            for i in range(first_index+1,last_index):
                charerc.add(s[i])

            res+=len(charerc)

        return res
                    
''' 
Approach:
since 3 length then we need to check only first and last char

so give every char a chance only once(set keep) to find the first and last occurrence eliminate duplicates), between these indexes you need to consider only unique char so keep a set for that and for every char, you add in res the len of set of middle char
'''

#solutio4: can make 3rd one better by precomputing first and last index


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        mp=set()
        n=len(s)

        for i in range(n):
            mp.add(s[i])
        occurences=[[-1,-1]for _ in range(26)]

        for i,char in enumerate(s):
            index=ord(char)-ord('a')
            if occurences[index][0]==-1: 
                #first occurence then make first point to this
                occurences[index][0]=i
            occurences[index][1]=i



        res=0
        for char in mp:
            index=ord(char)-ord('a')
            first_index,last_index=occurences[index]
            #we now have all the palindrome for current char, now take only unique ones
            charerc=set()
            if first_index==-1:
                continue
            for i in range(first_index+1,last_index):
                charerc.add(s[i])

            res+=len(charerc)

        return res
                    
'''extra thing learned here

For immutable objects (like integers, strings): [value for _ in range(n)] and [value] * n behave the same.

For mutable objects (like lists): [value] * n creates shared references, while [value for _ in range(n)] creates independent objects.

'''