"""
给定一个较长字符串big和一个包含较短字符串的数组smalls,
设计一个方法，根据smalls中的每一个较短字符串，对big进行搜索。
输出smalls中的字符串在big里出现的所有位置positions，
其中positions[i]为smalls[i]出现的所有位置。
"""




class Node(object):
    def __init__(self, idx=None):
        self.dic = {}
        self.word_end = False
        # self.word_idx = idx

class Trie(object):
    def __init__(self):
        self.root = {}
    def insert_word(self, word, idx):
        if word=="" : return
        cur_dic = self.root
        for char in word:
            cur_dic.setdefault(char, Node(idx))
            ob = cur_dic[char]
            # ob.word_idx = idx
            cur_dic = ob.dic
        ob.word_end = True
        ob.word_idx = idx


class Solution:
    def multiSearch(self, big, smalls):
        self.build_tree(smalls)
        rt = [[] for _ in range(len(smalls))]
        for i in range(len(big)):
            cur = self.trie.root
            for j in range(i, len(big)):
            # for location, char in enumerate(big[i:]):
                if big[j] in cur:
                    ob = cur[big[j] ]
                    # _idx = ob.word_idx
                    _end = ob.word_end
                    cur = ob.dic
                    if _end: rt[ob.word_idx].append(i)
                else: break
        return rt

    def build_tree(self, smalls):
        self.trie = Trie()
        for idx, word in enumerate(smalls):
            self.trie.insert_word(word, idx)
