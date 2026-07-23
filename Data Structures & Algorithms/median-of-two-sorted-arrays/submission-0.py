class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        lst = nums1 + nums2

        def find_median(lst):
            if not lst:
                return None
    
    # 1. 必須先排序
            sorted_lst = sorted(lst)
            n = len(sorted_lst)
            mid = n // 2
    
    # 2. 判斷奇偶數
            if n % 2 == 1:
        # 奇數個：直接取中間
                return sorted_lst[mid]
            else:
        # 偶數個：取中間兩個數的平均值
                return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2

                return statistics.median(l)

        return find_median(lst)


        