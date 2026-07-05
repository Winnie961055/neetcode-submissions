class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # a bit similar with Kth Largest Element in a Stream

        heap = []

        for point in points:
            distance = ((point[0] - 0) ** 2 + (point[1] - 0) ** 2) ** 0.5
            heapq.heappush(heap, [distance, [point[0], point[1]]])
        
        result = []

        for i in range(k):
            distance, point = heapq.heappop(heap)
            result.append(point)
        
        return result


