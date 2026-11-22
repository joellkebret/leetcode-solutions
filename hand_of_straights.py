from collections import Counter
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        freqs = Counter(hand)

        for start in sorted(freqs):
            while freqs[start] > 0:
                for card in range(start, start + groupSize):
                    if freqs[card] == 0:
                        return False
            
                    freqs[card] -=1

        return True
