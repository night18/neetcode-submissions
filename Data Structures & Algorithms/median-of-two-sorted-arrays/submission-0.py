class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 暴力法先試試
        nums = []
        len1, len2 = len(nums1), len(nums2)
        i, j = 0, 0

        while i < len1 and j < len2:
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        
        while i < len1:
            nums.append(nums1[i])
            i += 1

        while j < len2:
            nums.append(nums2[j])
            j += 1

        if len(nums) // 2 == len(nums) / 2:
            return (nums[len(nums) // 2] + nums[(len(nums) // 2) - 1]) / 2
        else:
            return nums[(len(nums) // 2)]
        
