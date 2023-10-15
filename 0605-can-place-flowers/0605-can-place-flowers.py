class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        size = len(flowerbed)
        for plant in range(size):
            if plant == 0 and (size != 1) and flowerbed[plant] == 0:
                if (flowerbed[plant+1] == 0):
                    flowerbed[plant] = 1
                    count+=1
                
            if plant != size-1:
                if flowerbed[plant] == 0:
                    if (flowerbed[plant-1] == 0) and (flowerbed[plant+1] == 0):
                        flowerbed[plant] = 1
                        count+=1
            
            if (plant == size-1) and flowerbed[plant] == 0:
                if flowerbed[plant-1] == 0:
                    flowerbed[plant] = 1
                    count+=1

        print(count)
        if count >= n:
            return True
        else:
            return False
                




        #     if (flowerbed[plant] == 0) and (plant <= (size-2) ):
        #         if (flowerbed[plant] == flowerbed[-1]) and (flowerbed[plant-1] == 0):
        #                 count+=1
        #                 break
        #         if flowerbed[plant] == 0:
        #             if (flowerbed[plant+1] == 0) and (flowerbed[plant-1]) == 0:
        #                 flowerbed[plant] = 1
        #                 count+=1
        # print(count)
        # if count >= n:
        #     return True
        # else:
        #     return False