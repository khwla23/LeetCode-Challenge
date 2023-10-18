class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        distinct_nums1 = list(set_nums1.difference(set_nums2))
        distinct_nums2 = list(set_nums2.difference(set_nums1))

        return [distinct_nums1, distinct_nums2]

        # #Step 1: for elements not present in the second list and vice versa
        # diff_nums1 = diff_nums2 = []
        # for x in num1:
        #     if x not in num2:
        #         diff_nums1.append(x)
        # for x in num2:
        #     if x not in num1:
        #         diff_nums2.append(x)

        # #step 2: removing the dupicates from the list
        # distinct_nums1 = list(set(distinct_nums1)) 
        # distinct_nums2 = list(set(distinct_nums2))  

        # return [distinct_nums1, distinct_nums2]
