

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {nums[i]:i for i in range(len(nums))}
        print(map1)
        for _,i in enumerate(nums):
            if target-i in map1 and _!=map1[target-i]:
                return [_,map1[target-i]]


# 参考答案
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


