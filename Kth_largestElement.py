import heapq #these are similar to priority queue

class kth_largest:
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.hqheap = []
        for (i in nums):
            self.add(i)  

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if((len(self.hqheap)) < self.k):
            heapq.heappush(self.hqheap,val)
        elif(self.hqheap[0]) < val:
            heapq.heappushpop(self.hqheap,val)
        if len(self.hqheap) < self.k:
            return -1
        else:
            return self.hqheap[0]