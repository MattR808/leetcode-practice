class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_nums = list(range(0,len(nums)+1,1))
        print(all_nums)

        set_of_nums = set(nums)

        set_of_all_nums =set(all_nums)

        missing_set = set_of_all_nums - set_of_nums

        return (list(missing_set))[0]

