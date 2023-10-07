class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool: #2darray
        #formula to use --> slope = (y2-y1)/(x2-x1) = (y-y1) / (x - x1)
        #find x1, y1
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        # find 2nd point -> x2, y2
        x2 = coordinates[1][0]
        y2= coordinates [1][1]
        x_diff_1 = x2 - x1
        y_diff_1 = y2 - y1
        for i in range (2,len(coordinates)):
            x_diff = (coordinates[i][0] - coordinates[i-1][0])
            y_diff = (coordinates[i][1] - coordinates[i-1][1])
            
            if (x_diff_1 * y_diff != y_diff_1 * x_diff): return False
        return True