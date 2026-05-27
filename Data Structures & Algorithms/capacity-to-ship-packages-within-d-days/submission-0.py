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
        
        count = 1
        while low < high:
            print("iteration: ", count)
            test = (low+high)//2
            print(low, high, test)
            d = 0
            s = 0
            for weight in weights:
                if s + weight > test:
                    d += 1 
                    s = weight
                else:
                    s += weight
            d += 1
            if d <= days:
                high = test
            else:
                low = test + 1 
            
            print(low, high, d)
            count+=1

        return low