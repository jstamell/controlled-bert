"""
__author__ = "Param Popat"
__version__ = "1.0"
__git__ = "https://github.com/parampopat/"
"""

from nltk.parse.generate import generate
from nltk import CFG, PCFG


class Generator(object):
    def __init__(self):
        self.grammar = None
        self.corpus = []

    def load_grammar(self, path: str, pcfg: bool = False):
        with open(path, 'r') as f:
            loaded_grammar = f.read()
        if pcfg:
            self.grammar = PCFG.fromstring(loaded_grammar)
        else:
            self.grammar = CFG.fromstring(loaded_grammar)

    def generate(self, num_sentences: int = None, depth: int = None):
        if num_sentences:
            for sentence in generate(self.grammar, n=num_sentences):
                self.corpus.append(' '.join(sentence))
        elif depth:
            for sentence in generate(self.grammar, depth=depth):
                self.corpus.append(' '.join(sentence))
        else:
            raise ValueError('Need either num_sentences or depth')

    def save(self, path: str):
        with open(path, 'w') as f:
            for sentence in self.corpus:
                f.write(sentence + '\n')
