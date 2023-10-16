class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for n in range(len(nums)):
            if (nums[n] != 0): #tracking non zero instead of zeros
                nums[n], nums[index] = nums[index], nums[n]
                index+=1

        # if (len(nums) != 1):
        #     for num in range(len(nums)):
        #         if nums[num] == 0: #removing zeros and appending them at the end of the list
        #             val = nums.pop(num)
        #             nums.append(val)
        