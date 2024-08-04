class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total = 0  # Initialize the net gas difference
        res = 0    # Initialize the starting index
        
        # Iterate through the gas stations
        for i in range(len(gas)):
            # Update the net gas difference
            total += (gas[i] - cost[i])
            
            # If the net gas difference becomes negative, reset to zero and update the starting index
            if total < 0:
                total = 0
                res = i + 1
        
        return res  