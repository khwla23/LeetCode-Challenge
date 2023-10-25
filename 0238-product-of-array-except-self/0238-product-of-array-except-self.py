class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_products = [1] * n
        suffix_products = [1] * n
        answer = [1] * n

        # prefix products
        prefix_product = 1
        for i in range(n):
            prefix_products[i] = prefix_product
            prefix_product *= nums[i]

        # suffix products
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            suffix_products[i] = suffix_product
            suffix_product *= nums[i]
        
        for i in range(n):
            answer[i] = prefix_products[i] * suffix_products[i]

        return answer

        # answer =[]
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if nums[i] != nums[j]:
        #             prod *= nums[j]
        #     answer.append(prod)
        # return answer