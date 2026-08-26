class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        number_set = set(nums)
        
        return len(number_set) != len(nums)


