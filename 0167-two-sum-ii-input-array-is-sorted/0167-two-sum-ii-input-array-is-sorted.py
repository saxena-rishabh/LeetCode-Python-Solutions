class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_pointer = 0
        end_pointer = len(numbers)-1
        while start_pointer < end_pointer:
            pair_sum = numbers[start_pointer] + numbers[end_pointer]
            if pair_sum == target:
                return [start_pointer + 1, end_pointer + 1]
            elif pair_sum > target:
                end_pointer -= 1
            elif pair_sum < target:
                start_pointer += 1