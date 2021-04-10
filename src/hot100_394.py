# 394. 字符串解码
#
# 给定一个经过编码的字符串，返回它解码后的字符串。
#
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
#
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
#
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

class Solution:
    def decodeString(self, s: str) -> str:
        l_s = list(s)
        stack = []
        for word in l_s:
            if word != ']':
                stack.append(word)
            else:
                #字符列表
                tem = []
                while stack[-1] != '[' and stack:
                    tem.append(stack.pop())
                tem = tem[::-1]
                #然后弹出'['
                stack.pop()
                #数字列表
                nums = []
                while len(stack) >= 1:
                    if '0' <= stack[-1] <= '9':
                        nums.append(stack.pop())
                    else:
                        break
                nums = nums[:: - 1]
                result = 0
                for num in nums:
                    result = result * 10 + int(num)
                ll = []
                while result:
                    ll += tem
                    result -= 1
                stack += ll
        return ''.join(stack)



Solution().decodeString("3[a2[c]]")

