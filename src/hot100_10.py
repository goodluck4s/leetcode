# *coding:utf-8 *

# 正则匹配

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p)==0:
            if len(s)==0:
                return True
            else:
                return False
        else:
            firstmatch = len(s)>=1 and (s[0]==p[0] or p[0] == ".")

            if len(p) >= 2 and p[1] == "*": #  第一个位置是*
                return firstmatch and self.isMatch(s[1:],p) or self.isMatch(s,p[2:])
            else:
                return firstmatch and self.isMatch(s[1:], p[1:])





print(Solution().isMatch("ss","s*"))



class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p)==0:
            return len(s)==0

        if len(s)==0:
            if p[-1]=="*" and len(p)==2:
                return True
            return len(p)==0

        fim = s[0]==p[0] or p[0]=="."

        if len(p)>=2 and p[1]=="*":
            return (fim and self.isMatch(s[1:],p)) or self.isMatch(s,p[2:])
        else:
            return fim and self.isMatch(s[1:],p[1:])

print(Solution().isMatch("asa","a.*a"))