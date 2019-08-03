class Solution:

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # looka at middle of array
        # if it's the median, stop
        # otherwise, do again with 1/2 the array
        if len(nums1) == 1 and len(nums2) == 1:
            return (nums1[0] + nums2[0]) / 2
        elif len(nums1) == 1 and len(nums2) == 2:
            return max(nums2[0], min(nums1[0], nums2[1]))
        elif len(nums1) == 2 and len(nums2) == 1:
            return max(nums1[0], min(nums2[0], nums1[1]))
        elif len(nums1) == 2 and len(nums2) == 2:
            tmp_arr = sorted(nums1 + nums2)
            return (tmp_arr[1] + tmp_arr[2]) / 2
        
        index1 = len(nums1) // 2
        index2 = len(nums2) // 2

        middle1 = nums1[index1]
        middle2 = nums2[index2]

        if middle1 == middle2:
            return middle1
        elif middle1 > middle2:
            return self.findMedianSortedArrays(nums1[:max(index1, 1)], nums2[index2:])
        else:
            return self.findMedianSortedArrays(nums1[index1:], nums2[:max(index2,1)])



x1 = list(range(5))
y1 = [0 for _ in range(5)]

x2 = list(range(5))
y2 = list(range(5))

x3 = list(range(0, 9))
y3 = list(range(1, 6))

x4 = [1,3]
y4 = [2]

print(Solution().findMedianSortedArrays(x1, y1))
print(Solution().findMedianSortedArrays(x2, y2))
print(Solution().findMedianSortedArrays(x3, y3))
print(Solution().findMedianSortedArrays(x4, y4))