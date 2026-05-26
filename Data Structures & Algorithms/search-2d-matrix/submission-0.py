class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        

        def colSearch():
            low = 0
            high = rows-1 

            while low < high:
                mid = (low+high+1)//2
                if matrix[mid][0] <= target:
                    low = mid
                else:
                    high = mid - 1 
            
            return low 
        
        idx = colSearch()
        
        def rowSearch():
            low = 0 
            high = cols - 1

            while low <= high:
                mid = (low+high)//2
                if matrix[idx][mid] == target:
                    return True 
                elif matrix[idx][mid] < target:
                    low = mid + 1 
                else:
                    high = mid - 1 
            
            return False 
                
        return rowSearch()