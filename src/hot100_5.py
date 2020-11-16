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
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        if s is None:
            return None
        if len(s)<=1:
            return s
        tmp_a=0
        tmp_b = 0
        for i in range(len(s)):
            a,b = self.fuc(s,i,i)
            a2,b2 = self.fuc(s,i,i+1)
            if b-a > tmp_b-tmp_a:
                tmp_b = b
                tmp_a = a
            if b2-a2 > tmp_b-tmp_a:
                tmp_b = b2
                tmp_a = a2
        return s[tmp_a:tmp_b+1]


    def fuc(self,s,i,j):
        while i>=0 and j<len(s) and s[i]==s[j]:
            i=i-1
            j=j+1
        return i+1,j-1


# 动态规划  p(i,j) = p(i+1,j-1) and s[i]==s[j]
# 略
