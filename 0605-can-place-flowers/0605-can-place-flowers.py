class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        size = len(flowerbed)
        for plant in range(size):
            #first flower but not the only
            if plant == 0 and (size != 1) and flowerbed[plant] == 0: 
                if (flowerbed[plant+1] == 0):
                    flowerbed[plant] = 1
                    count+=1
                
            if plant != size-1:
                if flowerbed[plant] == 0:
                    if (flowerbed[plant-1] == 0) and (flowerbed[plant+1] == 0):
                        flowerbed[plant] = 1
                        count+=1
            #last flower
            if (plant == size-1) and flowerbed[plant] == 0:
                if flowerbed[plant-1] == 0:
                    flowerbed[plant] = 1
                    count+=1

        print(count)
        if count >= n:
            return True
        else:
            return False
                