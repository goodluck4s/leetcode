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
        self.dic={}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        dic = self.dic
        for c in word:
            if c not in dic:
                dic[c]={}
            dic = dic[c]
        dic["*"]=None


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        dic = self.dic
        for c in word:
            if c in dic:
                dic=dic[c]
            else:
                return False
        if "*" in dic:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        dic = self.dic
        for c in prefix:
            if c in dic:
                dic = dic[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)