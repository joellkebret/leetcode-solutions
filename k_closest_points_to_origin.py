import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        
        # Reading the question i feel like we just calculate the euclidean distance
        # from the origin, push that onto th heap, and while heap is greater than k, we pop
        # then simply return the points
        heap = []

        for point in points:
            x,y = point
            distance = (0-x)**2 + (0-y)**2
            heapq.heappush(heap,(-distance,point))

            while len(heap) > k:
                heapq.heappop(heap)
        
        return [point for distance, point in heap]
