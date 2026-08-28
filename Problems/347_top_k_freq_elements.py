import heapq

class Solution(object):
    def topKFrequent1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}

        for i in range(len(nums)):
            
            if nums[i] in counts:
                counts[nums[i]] +=1
            else:
                counts.update({nums[i] : 1})

        items = list(counts.items())

        items.sort(key=lambda x: x[1], reverse=True)

        print(items)
        result = []

        for i in range(k):
            result.append(items[i][0])

        return result

    

    def topKFrequent(self, nums, k):
        counts = {}

        # Count frequencies
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        # Make heap: (-frequency, number)
        heap = []

        for number, frequency in counts.items():
            heap.append((-frequency, number))

        heapq.heapify(heap)

        result = []

        for i in range(k):
            frequency, number = heapq.heappop(heap)
            result.append(number)

        return result