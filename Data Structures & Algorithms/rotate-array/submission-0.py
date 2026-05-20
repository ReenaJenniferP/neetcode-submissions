class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        n = len(arr)
        rot = k % n 
        
        for i in range(0, (n-rot)//2):
            arr[i], arr[n-rot-1-i] = arr[n-rot-1-i], arr[i]
        
        for i in range(n-rot, (2*n-rot)//2):
            arr[i], arr[2*n-rot-1-i] = arr[2*n-rot-1-i], arr[i]

        for i in range(0, n//2):
            arr[i], arr[n-1-i] = arr[n-1-i], arr[i]

        return arr
        

# 1 2 3 4 5 6 7 8 

# by 3 

# 6 7 8 1 2 3 4 5 

# same as 

# # reverse 1st 5 and last 3 separately

# 5 4 3 2 1 8 7 6 

# #reverse whole thing 

# 6 7 8 1 2 3 4 5 