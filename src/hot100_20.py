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

