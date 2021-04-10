# 438. 找到字符串中所有字母异位词
#
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
#
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
#
# 说明：
#
#     字母异位词指字母相同，但排列不同的字符串。
#     不考虑答案输出的顺序。
#
# 示例 1:
#
# 输入:
# s: "cbaebabacd" p: "abc"
#
# 输出:
# [0, 6]
#
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

from string import ascii_lowercase


class Solution:
    def findAnagrams(self, s, p):
        ret = []
        k_dict = {}.fromkeys(ascii_lowercase, 0)
        for i in p:
            k_dict[i] += 1
        tmp = {}.fromkeys(ascii_lowercase, 0)
        left = right = 0
        while right < len(s):
            tmp[s[right]] += 1
            if tmp == k_dict:
                ret.append(left)
            if right - left + 1 == len(p):
                tmp[s[left]] -= 1
                left += 1
            right += 1
        return ret

Solution().findAnagrams("cbaebabacd" ,"abc")


a={"a":1,"b":2}
b = {"a":1,"b":2,"d":0}

print(a==b)