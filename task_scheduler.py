from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freqs = Counter(tasks)
        heap = []
        for count in freqs.values():
            heapq.heappush(heap, -count) # build max heap we cuz we want to schedule failrly
        
        t = 0
        cooldown = deque()

        while heap or cooldown:
            t+=1
            if cooldown and cooldown[0][1] <= t:
                count, _ = cooldown.popleft()
                heapq.heappush(heap,count)
            
            if heap:
                count = heapq.heappop(heap) + 1

                if count<0:
                    cooldown.append((count, t+n+1))
        
        return t
