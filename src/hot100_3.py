# *coding:utf-8 *

# 3. 无重复字符的最长子串
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。



# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if not s:
#             return 0
#
#         res = 0
#         i=0
#         tmp=[]
#         while i<len(s):
#             if s[i] not in tmp:
#                 tmp.append(s[i])
#                 i+=1
#                 if len(tmp)>res:
#                     res = len(tmp)
#             else:
#                 del tmp[0]
#         return res


class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        dic = {}
        i, j = 0, 0
        res = 0
        while j < len(s):
            while  j < len(s) and s[j] not in dic:
                dic[s[j]] = 0
                j = j + 1
                res = max(res, len(dic))
                continue
            dic.pop(s[i])
            i += 1
        return res


print(Solution().lengthOfLongestSubstring("pwwkew"))
