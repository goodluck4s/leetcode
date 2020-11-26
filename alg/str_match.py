# *coding:utf-8 *


def sunday(text, sub):
    sub_char_dic = {}
    for i, c in enumerate(sub):
        if c in sub_char_dic:
            sub_char_dic[c].append(i)
        else:
            sub_char_dic[c] = [i]

    def match(sub_text, sub):
        if len(sub_text) != len(sub):
            return False
        for i in range(len(sub_text)):
            if sub_text[i] != sub[i]:
                return False
        return True

    i = 0
    while i < len(text):
        text_sub = text[i:i + len(sub)]
        if match(text_sub, sub):
            return i, i + len(sub) - 1
        else:
            if i + len(sub) >= len(text):
                break
            after = text[i + len(sub)]
            if after in sub_char_dic:
                i = i + ((i + len(sub)) - (i + sub_char_dic[after][-1]))
            else:
                i = i + len(sub) + 1
    return -1, -1


print(sunday("this is a example", "example"))
