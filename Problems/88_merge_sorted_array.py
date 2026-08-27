class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        meaningful_end_1 = m - 1
        end_1 = len(nums1) - 1
        end_2 = n - 1

        while end_2 >= 0 and meaningful_end_1 >= 0:

            if nums1[meaningful_end_1] < nums2[end_2]:
                nums1[end_1] = nums2[end_2]
                end_2 -= 1
                end_1 -= 1

            else:
                nums1[end_1] = nums1[meaningful_end_1]
                meaningful_end_1 -= 1
                end_1 -= 1

        while end_2 >= 0:
            nums1[end_1] = nums2[end_2]
            end_2 -= 1
            end_1 -= 1