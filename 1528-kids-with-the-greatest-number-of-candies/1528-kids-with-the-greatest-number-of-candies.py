class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        for kid in range(len(candies)):
            candies[kid] += extraCandies
            candies[kid] = candies[kid] >= maxi
        return candies