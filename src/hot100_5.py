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


# 动态规划解法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]

