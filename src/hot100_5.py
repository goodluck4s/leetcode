# *coding:utf-8 *

#
# 5. 最长回文子串
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"
#

# 中心扩展
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s)<=1:
            return s
        res = ""
        for i in range(len(s)-1):
            a = self.expen(s,i,i)
            if len(a)>len(res):
                res=a
            b = self.expen(s,i,i+1)
            if len(b)>len(res):
                res=b
        return res


    def expen(self,s,i,j):
        while i>=0 and j<=len(s)-1 and s[i]==s[j]:
            i-=1
            j+=1
        return s[i+1:j]


Solution().longestPalindrome("cbbd")

# 动态规划  p(i,j) = p(i+1,j-1) and s[i]==s[j]
# 略
