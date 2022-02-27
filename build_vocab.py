import argparse
from pycocotools.coco import COCO
from collections import Counter


class Vocabulary(object):
    def __init__(self):
        self.word2idx = {}
        self.idx2word = {}
        self.idx = 0

    def add_word(self, word):
        if word not in self.word2idx:
            self.word2idx[word] = self.idx
            self.idx2word[self.idx] = word
            self.idx += 1

    def get_idx(self, word):
        if word in self.word2idx.keys():
            return self.word2idx[word]
        return self.word2idx['<unknown>']

    def get_word(self, idx):
        return self.idx2word[idx]

    def __len__(self):
        return len(self.word2idx)


def build_vocab(captions_path, threshold):
    coco = COCO(captions_path)
    counter = Counter()
    ids = coco.anns.keys()
    for annotation_idx in ids:
        caption = coco.anns[annotation_idx]['caption']
        words = (caption
                 .lower()
                 .replace('.', '')
                 .replace(',', '')
                 .replace(':', '')
                 .replace(';', '')
                 .replace('!', '')
                 .replace('?', '')
                 .split(' ')
                 )
        words.remove('')
        counter.update(words)
    words = [word for word, count in counter.items() if count >= threshold]
    vocab = Vocabulary()
    for word in words:
        vocab.add_word(word)
    vocab.add_word('<start>')
    vocab.add_word('<end>')
    vocab.add_word('<unknown>')
    return vocab
