import heapq
class MedianFinder:

    def __init__(self):
        self.lheap = []
        self.hheap = []

    def addNum(self, num: int) -> None:
        # add to the max heap
        heapq.heappush(self.lheap, -num)

        if self.hheap and -self.lheap[0] > self.hheap[0]:
            pnum = -heapq.heappop(self.lheap)
            heapq.heappush(self.hheap, pnum)
        
        if (len(self.hheap) - len(self.lheap)) > 1:
            pnum = heapq.heappop(self.hheap)
            heapq.heappush(self.lheap,-pnum)
        elif (len(self.lheap) - len(self.hheap)) > 1:
            pnum = -heapq.heappop(self.lheap)
            heapq.heappush(self.hheap, pnum)

    def findMedian(self) -> float:
        if (len(self.hheap) + len(self.lheap)) %2 == 0:
            return (-self.lheap[0] + self.hheap[0])/2
        else:
            if len(self.hheap) > len(self.lheap):
                return self.hheap[0]
            else:
                return -self.lheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
