#solutio1: use 2 map
# https://www.youtube.com/watch?v=689qj769Gt4
from sortedcontainers import SortedSet # type: ignore
from collections import defaultdict
class NumberContainers:

    def __init__(self):
        self.idx_to_num={} #index->number
        self.num_to_allidx=defaultdict(SortedSet) #number->all indexes this number stored on

    
        

    def change(self, index: int, number: int) -> None:
        #if index is already mapped to a number then gotta remove it from other map in set
        if index in self.idx_to_num:
            prev_num=self.idx_to_num[index]
            self.num_to_allidx[prev_num].discard(index)

            #what if after removing number->{} then delete the entry only

            if not self.num_to_allidx[prev_num]:
                del self.num_to_allidx[prev_num]
        
        #if index there replacing, if not there adding
        self.idx_to_num[index]=number
        self.num_to_allidx[number].add(index)
        

    def find(self, number: int) -> int:

        if number in self.num_to_allidx and self.num_to_allidx[number]:
            return self.num_to_allidx[number][0]

        return -1

        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)


#solution2: use heap

import heapq
class NumberContainers:

    def __init__(self):
        self.idx_to_num={} #index->number
        self.num_to_allidx=defaultdict(list) #number->min heap of indices

    
        

    def change(self, index: int, number: int) -> None:
        #update the number at the index

        self.idx_to_num[index]=number

        heapq.heappush(self.num_to_allidx[number],index)
        

    def find(self, number: int) -> int:

        #get the desired min heap for the number
        pq=self.num_to_allidx[number]

        while pq:
            idx=pq[0]

            # Check if the index still has the correct number
            if self.idx_to_num[idx]==number:
                return idx

            #if the number is no longer valid then remove it

            heapq.heappop(pq)

        return -1

        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

