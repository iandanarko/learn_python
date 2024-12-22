# min_heap is tree with root is always the smallest value
import heapq


minHeap = [4, 5, 3, 1, 2]
heapq.heapify(minHeap) # turn arr to heap now root is 1
print(minHeap[0]) # return 1
heapq.heappush(minHeap, 0) 
print(minHeap[0]) # return 0
val = heapq.heappop(minHeap)
print(val) # return 0
print(minHeap[0]) # return 1

# python desn't support maxHeap so use minus instead 