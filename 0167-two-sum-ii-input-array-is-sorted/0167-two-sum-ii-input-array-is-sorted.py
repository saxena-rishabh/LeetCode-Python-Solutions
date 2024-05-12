class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_pointer = 0
        end_pointer = len(numbers)-1
        while start_pointer < end_pointer:
            if numbers[start_pointer] + numbers[end_pointer] == target:
                return [start_pointer + 1, end_pointer + 1]
            elif numbers[start_pointer] + numbers[end_pointer] > target:
                end_pointer -= 1
            elif numbers[start_pointer] + numbers[end_pointer] < target:
                start_pointer += 1