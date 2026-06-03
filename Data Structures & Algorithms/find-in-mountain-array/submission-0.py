class Solution:
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        l = arr.length()
        
        low, high = 0, l-1

        while low < high:
            mid = (low+high)//2

            if arr.get(mid) < arr.get(mid+1):
                low = mid + 1
            else:
                high = mid

        peak = low

        low, high = 0, peak

        while low <= high:
            mid = (low+high)//2
            m = arr.get(mid)

            if target == m:
                return mid
            elif target > m:
                low = mid + 1
            else:
                high = mid - 1

        low, high = peak+1, l-1

        while low <= high:
            mid = (low+high)//2
            m = arr.get(mid)
            
            if target == m:
                return mid
            elif target > m:
                high = mid - 1
            else:
                low = mid + 1
        return -1
