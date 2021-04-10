# 32. 最长有效括号
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
# 示例 1:
#
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#
# 示例 2:
#
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#


# 回朔法 O(2^n)
class Solution2:

    def isValid(self, s: str) -> bool:
        dic = {
            ")":"(",
            "]":"[",
            "}":"{",
               }
        tmp = []
        for c in s:
            if c not in dic:
                tmp.append(c)
            else:
                top = tmp.pop() if len(tmp)>0 else "*"
                if top == dic[c]:
                    continue
                else:
                    return False
        return len(tmp)==0

    def longestValidParentheses(self, s: str) -> int:
        if len(s)<=1:
            return 0
        if self.isValid(s):
            return len(s)
        else:
            a = self.longestValidParentheses(s[1:])
            b= self.longestValidParentheses(s[:-1])
            return  a if a>b else b

print(Solution2().longestValidParentheses("(()))())("))


#



def func(s):
    if not s:
        return 0

    dp = [0]*len(s)

    for i in range(len(s)):

        if s[i]==")":
            if i>=1:
                if s[i-1]=="(":
                    dp[i]=2 if i-2<0 else dp[i-2]+2
                if s[i-1]==")":
                    if dp[i-1]>0 and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=="(":
                        dp[i] = dp[i-1]+2 + (dp[i-dp[i-1]-2] if i-dp[i-1]-2>=0 else 0)
    return max(dp)

print(func("(((()))("))









class Solution:

    def longestValidParentheses(self, s: str) -> int:

        if s is None or len(s)<1:
            return 0

        dp=[0]*len(s)
        for i in range(1,len(s)):

            if s[i] == "(":
                continue
            if s[i-1]==")":
                if dp[i-1]>0 and i-dp[i-1]>0 and s[i-dp[i-1]-1]=="(":
                    dp[i] = dp[i-1]+2 + (dp[i-dp[i-1]-2] if i-dp[i-1]-2>=0 else 0)
            else:
                dp[i]= 2 if i<2 else dp[i-2]+2
        return max(dp)


print(Solution().longestValidParentheses("(()))())("))