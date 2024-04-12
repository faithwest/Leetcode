import heapq

def topKFrequent(nums, k):
    # Step 1: Count frequencies using a hash map
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    # Step 2: Construct min-heap with size k
    heap = []
    for num, freq in freq_map.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    # Step 3: Extract elements from heap
    result = [item[1] for item in heap]

    return result

# Example usage:
nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print(topKFrequent(nums1, k1))  # Output: [1, 2]

nums2 = [1]
k2 = 1
print(topKFrequent(nums2, k2))  # Output: [1]
