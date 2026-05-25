class Solution:
    def carFleet(self, target: int, pos: List[int], spe: List[int]) -> int:
        cars = sorted(zip(pos, spe), reverse=True)
        fleets = 0
        fleet_time = 0

        for p, s in cars:
            time = (target-p)/s

            if time > fleet_time:
                fleets += 1
                fleet_time = time 

        
        return fleets