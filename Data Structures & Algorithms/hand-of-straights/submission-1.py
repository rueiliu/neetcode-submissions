'''
match:
    min-heap problem

1. first check if the len(hand) is divisible by 4
2. create counter(to count the amt of elements) and heap
3. while min - heap exist, check if the first element in counter is 0 (if it is then pop heap and continue)
4. then use a for loop to check if the first element of the heap can form a qualified group(by checking counter == 0 or not)




'''


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        #create counter and heap

        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:

            first = min_heap[0]

            if count[first] == 0: # then remove heap
                heapq.heappop(min_heap)
                continue

            for i in range(first, first + groupSize):
                
                if count[i] == 0:
                    return False

                count[i] -= 1

        return True





        