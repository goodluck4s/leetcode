# 49. 字母异位词分组
#
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
# 示例:
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#

a = "aba"
print(sorted(a))

class Solution:
    def groupAnagrams(self, strs):

        if not strs:
            return []
        res={}

        for i in strs:
            i_ = "".join(sorted(i))
            if i_ not in res:
                res[i_] = [i]
            else:
                res[i_].append(i)
        print(res)
        return list(res.values())


print(Solution().groupAnagrams( ["eat", "tea", "tan", "ate", "nat", "bat"]))