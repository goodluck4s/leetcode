class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return

        dic={
            ")":"(",
            "]": "[",
            "}": "{",
        }

        stack=[]

        for c in s:
            if c not in dic:
                stack.append(c)
            else:
                if len(stack)>0 and dic[c]==stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0




class Solution2:
    def isValid(self, s: str) -> bool:
        """
        只针对 ()()()括号的高效写法
        :param s:
        :return:
        """

        bol = 0
        for c in s:
            if c =="(":
                bol+=1
            else:
                bol-=1
            if bol<0:
                return False
        return bol==0

