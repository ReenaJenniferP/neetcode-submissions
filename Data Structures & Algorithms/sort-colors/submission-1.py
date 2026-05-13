class Solution:
    def sortColors(self, arr: List[int]) -> None:
        zero = 0
        one = 0
        two = len(arr)-1

        while one <= two:
            if arr[one] == 0:
                arr[one], arr[zero] = arr[zero], arr[one]
                zero += 1
                one += 1
            elif arr[one] == 2:
                arr[one], arr[two] = arr[two], arr[one]
                two -= 1
            else:
                one += 1

        