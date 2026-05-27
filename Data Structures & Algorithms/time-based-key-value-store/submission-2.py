class TimeMap:

    def __init__(self):
        self.timeMp = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timeMp[key]
        if not arr or arr[0][0] > timestamp:
            return ""

        low = 0
        high = len(arr)-1

        while low < high:
            mid = (low+high+1)//2
            if arr[mid][0] <= timestamp:
                low = mid
            else:
                high = mid - 1 

        return arr[low][1]
        
        
        
