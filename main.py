class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index in range(len(nums)):
            number = nums[index]
            complement = target - number
            if complement in hashmap:
                return index, hashmap[complement]
            else:
                hashmap[number] = index
        return 'Not valid'