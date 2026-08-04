class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,num in enumerate (nums):
            complement = target - num  #core logic of this sum
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i # this is how we add elements to the dictionary