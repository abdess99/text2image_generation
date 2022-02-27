import argparse

class Vocabulary (object):
    def __init__(self):
        self.word2idx = {}
        self.idx2word = {}
        self.idx = 0

    def add_word(self, word):
        if word not in self.word2idx:
            self.word2idx[word]= self.idx
            self.idx2word[self.idx]=word
            self.idx+=1

    def get_idx(self, word):
        if word in self.word2idx.keys():
            return self.word2idx[word]
        return self.word2idx['<unknown>']

    def get_word(self, idx):
        return self.idx2word[idx]

    def __len__(self):
        return len(self.word2idx)


