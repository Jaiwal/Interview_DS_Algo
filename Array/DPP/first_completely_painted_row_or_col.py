'''
Visited Matrix Techniques

1. Visited Matrix for Tracking Painted Cells
   Method: Utilize a 2D visited matrix to track which cells have been painted.
   Row/Column Completion Check: Use the `all()` function to verify if all cells in a row or column are painted.
   Time Complexity: O(n * m + k * (n + m))
   where n is the number of rows, m is the number of columns, and k is the number of painting operations.

2. Row/Column Counters
   Method: Maintain row_count and col_count arrays to keep track of painted cells in each row and column.
   Time Complexity: O(n * m + k)

3. Optimized Last Painted Index
   Method: Map array values to their respective indices to efficiently compute the last index needed for painting rows and columns.
   Time Complexity: O(k + n * m)

Python-Specific Concepts

Using defaultdict
Utilize defaultdict(list) for automatic list initialization.
Example:
from collections import defaultdict
mp = defaultdict(list)
mp[key].append(value)

Storing Positions with Tuples
Store matrix positions using tuples.
Example:
mp[num] = (row, col)

Enumerate for Iteration
Use enumerate() to iterate with both index and value.
Example:
for index, value in enumerate(arr):
    # process value

Dictionary Comprehension
Create mappings of values to indices in a single line.
Example:
mp = {num: index for index, num in enumerate(arr)}

'''

#solution1: TLE on 2 cases
from typing import List
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        visited=[[False for _ in range(len(mat[0]))]for _ in range(len(mat))]

        mp=defaultdict(list)

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                mp[mat[row][col]]=(row,col)

        for index,num in enumerate(arr):
            row,col=mp[num]
            visited[row][col]=True
            entirerow,entirecol=self.is_row_or_col_painted(visited,row,col)
            if entirerow or entirecol:
                return index



        return -1

    def is_row_or_col_painted(self, visited, row, col):
        is_row_painted = all(visited[row][c] for c in range(len(visited[row])))   
        is_col_painted = all(visited[r][col] for r in range(len(visited)))
    
        return is_row_painted, is_col_painted


        
#solutio2: use extra space

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        row_count=[0]*len(mat)
        col_count=[0]*len(mat[0])

        mp={}

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                mp[mat[row][col]]=(row,col)

        for index,num in enumerate(arr):
            row,col=mp[num]

            row_count[row]+=1
            col_count[col]+=1
            '''A row is fully painted when row_count[row] equals the number of columns
               in the matrix: len(mat[0]).

                A column is fully painted when col_count[col] equals the number of rows in the
                 matrix: len(mat).
            
            if row_count[row]==len(mat) or col_count[col]==len(mat[0]):
                return index

            '''
            if row_count[row]==len(mat[0]) or col_count[col]==len(mat):
                return index
        return -1

        
#solution3: do the reverse tech instead

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        mp=defaultdict(int)

        for index,num in enumerate(arr):
            mp[num]=index
        
        minIndex=float('inf')
        #check for every row, what is the last index that it will get entirely painted

        for row in range(n):
            lastIndex=-float('inf')

            for col in range(m):
                index=mp[mat[row][col]]
                lastIndex=max(lastIndex,index)

            minIndex=min(minIndex,lastIndex)
        #check for every col, what is the last index that it will get entirely painted

        for col in range(m):
            lastIndex=-float('inf')

            for row in range(n):
                index=mp[mat[row][col]]
                lastIndex=max(lastIndex,index)

            minIndex=min(minIndex,lastIndex)   

        return  minIndex  