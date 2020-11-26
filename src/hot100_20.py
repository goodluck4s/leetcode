class Solution:
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

