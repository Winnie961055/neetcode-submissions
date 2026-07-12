class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        from collections import Counter
        count = Counter(tasks)

        # Heap + Queue

        heap = [- i for i in count.values()]
        heapq.heapify(heap)
        queue = collections.deque()
        time = 0
        heapCount = 0

        while heap or queue:

            time += 1

            # check queue first
            if queue and queue[0][1] == time: 
                queueCount, readytime = queue.popleft()
                heapq.heappush(heap, queueCount)
            
            # work
            if heap: 
                heapCount = heapq.heappop(heap)
                heapCount += 1
                if heapCount: # if heapCount = 0, don't have to append to the queue
                    queue.append((heapCount, time + n + 1)) # (heapCount, time + n) is a tuple, not 2 parameters
        
        return time


        