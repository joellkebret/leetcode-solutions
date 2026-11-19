import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap,-stone)
        
        while heap:
            if len(heap)>=2:
                y = -heapq.heappop(heap)
                x = -heapq.heappop(heap)

                if x == y:
                    continue
                else:
                    heapq.heappush(heap, -(y-x))
            
            if len(heap) == 1:
                return -heap[0]
        
        return 0
        
