class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-s for s in stones]
        self.minHeap = stones
        heapq.heapify(self.minHeap) # python only has min heap

        while len(self.minHeap) > 1:
            y = heapq.heappop(self.minHeap)
            x = heapq.heappop(self.minHeap)
            if -x < -y:
                heapq.heappush(self.minHeap, y-x)
        
        if not self.minHeap:
            return 0
        return -self.minHeap[0] # use this to get the smallest num in the heap

            
