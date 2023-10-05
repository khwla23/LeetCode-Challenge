class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_array =[]
        for i in range (n):
            new_array.append(nums[i])
            new_array.append(nums[n])
            n+=1
            
        return new_array
        