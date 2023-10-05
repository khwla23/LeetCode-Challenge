class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)  #size
        d_sum = 0
        size_mat = n-1 # 0-3
        for i in range(n):
            d_sum += mat[i][i]
            d_sum += mat[i][size_mat - i]  # secondary diagonal
#check for an odd array
        if (n % 2 == 1): #for an odd array like 3x3, 5x5 sub common diagonal value
            d_sum -= mat[n // 2][n // 2] #mat[1][1]; at which index
        return d_sum
