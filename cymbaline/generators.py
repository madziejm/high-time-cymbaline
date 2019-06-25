from cymbaline.data import DataProvider
from cymbaline.language import LanguageToolkit

import random


class Generator:
    def __init__(self, context_word=None, context_vector=None):
    """Initiates Generator with either single word or vector, which defines the context"""
        if(context_word == None and context_vector == None):
            raise TypeError("Either `context_word` or `context_vector` argument is required.")

        self._context_word = context_word
        self._context_vector = context_vector

        self.lt = LanguageToolkit(context_word=context_word, context_vector=context_vector)
    
    @property
    def context_vector(self):
        return self.context_vector

    @context_vector.setter
    def context_vector(self, value):
        self.lt = LanguageToolkit(context_word=None, context_vector=value)

    @property
    def context_word(self):
        return self.context_vector
    
    @context_word.setter
    def context_word(self, value):
        self.lt = LanguageToolkit(context_word=value, context_vector=None)

    def generate(self):
        raise NotImplementedError("Abstract `Generator` base class method has been called.")

    def _generate_n_syllables_stich(self, n):
        stich = ""

        while n > 0:
            word_syllables_count = random.randint(1, n)
            if stich:
                stich += " "
            candidate_words = self.lt.n_syllables_top_related_words(syllables_count=word_syllables_count)
            stich += random.choice(candidate_words)
            n -= word_syllables_count
        
        return stich
    

class HaikuGenerator(Generator):

    def __init__(self, context_word=None, context_vector=None):
        super().__init__(context_word, context_vector)

    def generate(self):
        haiku = self._generate_n_syllables_stich(5)
        haiku += '\n'
        haiku += self._generate_n_syllables_stich(7)
        haiku += '\n'
        haiku += self._generate_n_syllables_stich(5)
        
        return haiku
