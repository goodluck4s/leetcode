# 208. 实现 Trie (前缀树)
#
# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
#
# 示例:
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");
# trie.search("app");     // 返回 true

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nexts = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.nexts
        for i in word:
            if i not in p:
                p[i] = {}
            p = p[i]

        p["#"] = "#"



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.nexts
        for i in word:
            if i in p:
                p = p[i]
            else:
                if "#" in p:
                    return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.nexts
        for i in prefix:
            if i in p:
                p = p[i]
            else:
                return False
        return True