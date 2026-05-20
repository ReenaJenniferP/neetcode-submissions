class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        res = 0

        left = 0
        right = len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                    left += 1

            right -= 1
            res += 1

        return res