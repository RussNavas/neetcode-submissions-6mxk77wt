class Solution:
        
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Build hashmap: position -> arrival time
        time_map = {}
        for i in range(len(position)):
            time_map[position[i]] = (target - position[i]) / speed[i]
        
        # Sort positions in descending order (front to back)
        sorted_positions = sorted(time_map.keys(), reverse=True)
        
        fleets = 0
        max_time = 0  # time of the slowest fleet ahead
        
        for pos in sorted_positions:
            time = time_map[pos]
            
            # If this car arrives later than the fleet ahead,
            # it starts a new fleet
            if time > max_time:
                fleets += 1
                max_time = time
            # Otherwise it catches up and merges into the fleet ahead
        
        return fleets