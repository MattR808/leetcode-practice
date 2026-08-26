class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):

                    if nums[i] + nums[j] == target:
                        result = [i,j]

        return result
    
    def twoSum(self, nums, target):
        nums_map = dict()
        for i in range(len(nums)):
            if target - nums[i] in nums_map:
                return [nums_map[target-nums[i]], i]
            else:
                nums_map.update({nums[i] : i})



        