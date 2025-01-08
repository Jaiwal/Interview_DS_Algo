#solution1: use appraoch from word search1 and so it for every word and once you return true
#clear the state of the board

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res=[]

        for word in words:
            if self.exist(board,word):
                res.append(word)

        return res


    def exist(self, board: List[List[str]], word: str) -> bool:

        n=len(board)
        m=len(board[0])

        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0] and self.wordExist(board,word,i,j,0,n,m):
                    return True

        return False

    def wordExist(self,board,word,row,col,index,n,m):

        if index==len(word):
            return True

        if row<0 or row>=n or col<0 or col>=m:
            return False
        
        if board[row][col]!=word[index] or board[row][col]=='$':
            return False

        temp=board[row][col]
        board[row][col]='$'

        for dr,dc in [(1,0),(-1,0),(0,-1),(0,1)]:
            newrow=row+dr
            newcol=col+dc
            if self.wordExist(board,word,newrow,newcol,index+1,n,m):
                board[row][col] = temp
                return True
        
        board[row][col]=temp
        return False
        
        
#solution2: using trie to only explore fewer paths as above one gives TLE


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.word = ""

class Solution:
    def __init__(self):
        self.result = []
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def insert(self, root, word):
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.endOfWord = True
        node.word = word

    def dfs(self, board, i, j, node):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == '$' or board[i][j] not in node.children:
            return
        
        node = node.children[board[i][j]]
        if node.endOfWord:
            self.result.append(node.word)
            node.endOfWord = False  # Avoid duplicate results

        temp = board[i][j]
        board[i][j] = '$'  # Mark cell as visited
        
        for dr, dc in self.directions:
            self.dfs(board, i + dr, j + dc, node)
        
        board[i][j] = temp  # Restore cell after backtracking

    def findWords(self, board, words):
        root = TrieNode()
        for word in words:
            self.insert(root, word)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    self.dfs(board, i, j, root)
        
        return self.result
