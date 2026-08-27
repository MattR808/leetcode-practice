class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        

        while left < right:
            middle = (left+right) // 2
            if nums[middle] == target:
                return middle
            
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle -1
        print(left,right)
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        else:
            return -1
            
        
            
        