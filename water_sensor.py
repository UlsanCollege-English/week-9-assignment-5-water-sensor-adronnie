import heapq

def streaming_median(nums):
    if not nums:
        return []

    low = []   # max-heap (store as negatives)
    high = []  # min-heap
    result = []

    for x in nums:
        # Step 1: Push to correct heap
        if not low or x <= -low[0]:
            heapq.heappush(low, -x)
        else:
            heapq.heappush(high, x)

        # Step 2: Balance the heaps
        if len(low) > len(high) + 1:
            heapq.heappush(high, -heapq.heappop(low))
        elif len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))

        # Step 3: Compute median
        if len(low) == len(high):
            median = (-low[0] + high[0]) / 2.0
        else:
            median = float(-low[0])  # low has one extra element

        # Step 4: Append
        result.append(median if median % 1 else int(median))

    return result
