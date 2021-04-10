# *coding:utf-8 *

# class Solution:
#     def letterCombinations(self, digits: str):
#         if not digits:
#             return list()
#
#         phoneMap = {
#             "2": "abc",
#             "3": "def",
#             "4": "ghi",
#             "5": "jkl",
#             "6": "mno",
#             "7": "pqrs",
#             "8": "tuv",
#             "9": "wxyz",
#         }
#
#         def backtrack(index: int):
#             if index == len(digits):
#                 combinations.append("".join(combination))
#             else:
#                 digit = digits[index]
#                 for letter in phoneMap[digit]:
#                     combination.append(letter)
#                     backtrack(index + 1)
#                     combination.pop()
#
#         combination = list()
#         combinations = list()
#         backtrack(0)
#         return combinations
#
# print(Solution().letterCombinations("234"))
# print(len(Solution().letterCombinations("234")))
#
#
#
# class Solution2:
#     def letterCombinations(self, digits: str):
#         if not digits:
#             return list()
#
#         phoneMap = {
#             "2": "abc",
#             "3": "def",
#             "4": "ghi",
#             "5": "jkl",
#             "6": "mno",
#             "7": "pqrs",
#             "8": "tuv",
#             "9": "wxyz",
#         }
#
#         def fuc(tmp,d):
#             res=[]
#             for i in tmp:
#                 for c in phoneMap[d]:
#                     res.append(i+c)
#             return res
#
#         tmp=[c for c in phoneMap[digits[0]]]
#         for i in range(1,len(digits)):
#             tmp=fuc(tmp,digits[i])
#         return tmp
#
# print(Solution2().letterCombinations("234"))
# print(len(Solution2().letterCombinations("234")))


class Solution3:
    def letterCombinations(self, digits: str):
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res=[]
        tmp=[]

        def f(d):
            if len(tmp)==len(digits):
                res.append(tmp[:])
                return
            for l in phoneMap[digits[d]]:
                tmp.append(l)
                f(d+1)
                tmp.pop()
        f(0)
        return res






print(Solution3().letterCombinations("23"))
print(len(Solution3().letterCombinations("232")))