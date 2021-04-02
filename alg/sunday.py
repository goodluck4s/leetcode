# -- coding: utf-8 --


def find(main_str, k):
    if not main_str:
        return -1, -1

    if not k:
        return -1, -1

    map = {}
    for _, i in enumerate(k):
        map[i] = _

    main_offset = 0

    while main_offset <= len(main_str) - len(k):

        k_off = 0

        res = True
        while k_off < len(k):
            if k[k_off] == main_str[k_off + main_offset]:
                k_off += 1
            else:
                # 在这个k_off 没匹配上
                res = False
                break
        if res:
            return main_offset, len(k)
        else:
            imp = main_str[main_offset + len(k)]
            if imp in map:
                main_offset += len(k) - map[imp]
            else:
                main_offset += len(k) + 1

    return -1, -1


print(find("this is a abda hahahahah", "a a"))
