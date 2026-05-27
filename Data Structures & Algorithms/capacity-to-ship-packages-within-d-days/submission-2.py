# class Solution:
#     def shipWithinDays(self, weights: List[int], days: int) -> int:
#         # low = max(weights)
#         # high = sum(weights)

#         # while low < high:
#         #     test = (low+high)//2


            
            



#         #     return low 

#         test = 10
#         d = 0
#         s = 0
#         for weight in weights:
#             if s + weight > test:
#                 d += 1 
#                 s = weight
#             else:
#                 s += weight
        
#         d += 1

#         print(test, d)
#         return 0


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        
        while low < high:
            test = (low+high)//2

            d = 1
            s = 0
            for weight in weights:
                if s + weight > test:
                    d += 1 
                    s = 0
                s += weight

            if d <= days:
                high = test
            else:
                low = test + 1

        return low