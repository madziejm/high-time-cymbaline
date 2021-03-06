from cymbaline.data import DataProvider
from cymbaline.language import LanguageToolkit

import random


class Generator:
    def __init__(self, context_words):
        """Initiates Generator with either list of words defining the context"""
        self.context_words = context_words
        self.lt = LanguageToolkit()


    def generate(self) -> str:
        raise NotImplementedError("Abstract `Generator` base class method has been called.")

    def _generate_n_syllable_verse(self, n: int) -> str:
        verse = ""

        while n > 0:
            word_syllable_count = 1 if n == 1 else random.randint(2, n)
            # else:
            #     word_syllable_count = 
            # non-empty verse conditional
            if verse:
                verse += " "
            candidate_words = self.lt.n_syllable_top_related_words(syllable_count=word_syllable_count, context_words=self.context_words)
            verse += random.choice(candidate_words)
            n -= word_syllable_count
        
        return verse
    

class HaikuGenerator(Generator):

    def generate(self) -> str:
        haiku = self._generate_n_syllable_verse(5)
        haiku += '\n'
        haiku += self._generate_n_syllable_verse(7)
        haiku += '\n'
        haiku += self._generate_n_syllable_verse(5)
        
        return haiku
