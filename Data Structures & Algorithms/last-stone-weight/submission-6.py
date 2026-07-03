class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) > 1:
            stones = [-s for s in stones]
        else:
            return stones[-1]
        self.minHeap = stones
        heapq.heapify(self.minHeap) # python only has min heap

        while len(self.minHeap) > 1:
            y = heapq.heappop(self.minHeap)
            x = heapq.heappop(self.minHeap)
            if -x < -y:
                heapq.heappush(self.minHeap, y-x)
        
        if not self.minHeap:
            return 0
        return -self.minHeap[-1]

            
