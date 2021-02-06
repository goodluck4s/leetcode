# 76.
# 最小覆盖子串
#
# 给你一个字符串
# s 、一个字符串
# t 。返回
# s
# 中涵盖
# t
# 所有字符的最小子串。如果
# s
# 中不存在涵盖
# t
# 所有字符的子串，则返回空字符串
# "" 。
#
# 注意：如果
# s
# 中存在这样的子串，我们保证它是唯一的答案。
#
#
#
# 示例
# 1：
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"

import sys

class Solution():

    def minWindow(self, s, t):
        ori = {}
        cnt = {}

        def check():
            for k, v in ori.items():
                if cnt.get(k, 0) < v:
                    return False
            return True

        for c in t:
            ori[c] = ori.get(c, 0) + 1

        l = 0
        r = -1
        reslen = sys.maxsize
        ansL = -1
        ansR = -1
        sLen = len(s)

        while r < sLen:
            r += 1
            if r < sLen and s[r] in ori:
                cnt[s[r]] = cnt.get(s[r], 0) + 1

            while check() and l <= r:
                if r - l + 1 < reslen:
                    reslen = r - l + 1
                    ansL = l
                    ansR = l + reslen
                cnt[s[l]] = cnt.get(s[l], 0) - 1

                l += 1
        return "" if ansL == -1 else s[ansL: ansR]


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
