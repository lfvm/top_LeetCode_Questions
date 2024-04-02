"""
703. Kth Largest Element in a Stream


Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""
import heapq

class KthLargest:

    """ 
        We are going to use a min heap of lenght k. 

        That way we always know that the kth largest element 
        is the minum element of the heap. That element can be retrieved 
        in O(1).

        Popping an element from a heap is log(n). 

        So in the constructor, when we make the heap length = k 
        we are going to do that in the worst case scenario n * log(n) times 
    """

    def __init__(self, k: int, nums: List[int]):
        
        self.minHeap, self.k = nums,k 
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        
        heapq.heappush(self.minHeap,val)
        if  len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # we know that the min value in a heap is always on index 0 
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)