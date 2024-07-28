class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_end_index = m - 1
        nums2_end_index = n - 1
        global_end_index = m + n - 1

        while nums1_end_index >= 0 and nums2_end_index >= 0:
            if nums1[nums1_end_index] > nums2[nums2_end_index]:
                nums1[global_end_index] = nums1[nums1_end_index]
                nums1_end_index -= 1
            else:
                nums1[global_end_index] = nums2[nums2_end_index]
                nums2_end_index -= 1
            global_end_index -= 1

        # If there are remaining elements in nums2
        while nums2_end_index >= 0:
            nums1[global_end_index] = nums2[nums2_end_index]
            nums2_end_index -= 1
            global_end_index -= 1
