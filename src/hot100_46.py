# 全排列


class Solution2:
    def permute(self, nums):
        if nums is None or len(nums) == 0:
            return None
        if len(nums) == 1:
            return [nums]

        n = len(nums)

        def fuc(tmp, d):
            res = []
            for t in tmp:
                for i in range(len(t) + 1):
                    t1 = t[:]
                    t1.insert(i, d)
                    res.append(t1)

            return res

        tmp = [[nums[0]]]

        for i in list(range(1, n)):
            tmp = fuc(tmp, nums[i])

        print(tmp)
        print(len(tmp))
        return tmp


print(Solution2().permute([1, 2, 3]))

print("------------------------------")



class Solution:
    def permute(self, nums):
        if not nums:
            return []
        if len(nums)==1:
            return [nums]
        ans = []
        for i,n in enumerate(nums):
            a = [[n]+p for p in self.permute(nums[:i]+nums[i+1:])]
            ans.extend(a)
        return ans


print(Solution().permute([1, 2, 3]))
