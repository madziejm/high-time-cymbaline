import numpy as np
from collections import defaultdict
from cymbaline.language import LanguageToolkit
import os



class DataProvider:
    
    path = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        self._dictvec = None
        self._revenge = None
        self._zemsta_rhymes = defaultdict(list)
        self._personal_corpora_rhymes = defaultdict(list)
        self._teddy_rhymes = defaultdict(list)
        self._teddy = None
        self._personal_corpora = None
        self._words = None
        self.toolkit = LanguageToolkit()

    def get_vectors_for_words(self) -> dict:
        '''
        Make dictionary that contains {word, np.array[vector]}.
        We don't need to know vectors of words shorter than 3
        and that contains characters different that letters.
        '''
        if not self._dictvec:
            dict_poleval = {}
            counter = 0
            with open(os.path.join(self.path,'../data/poleval_base_vectors.txt'), encoding='utf8') as f:
                f.readline()
                for line in f:
                    L = line.split()
                    word = L[0]
                    if len(word) >= 3 and word.isalpha():
                        doc = [float(s) for s in L[1:]]
                        vec = np.array(doc, dtype='single')
                        dict_poleval[word] = vec
                        counter += 1
                        if counter % 10000 == 0:
                            print(counter, " I")
                    else:
                        next

            self._dictvec = dict_poleval
        return self._dictvec

    def get_personal_corpora_sentences(self):
        '''
        Make list that contains sentences from personal corpora.
        '''
        if not self._personal_corpora:
            tab_personal_corpora = []
            counter = 0
            with open(os.path.join(self.path, '../data/personal_corpora.txt'), encoding='utf8') as f:
                for line in f:
                    line = line[:-3] + line[-2] #erase spaces and '/n' characters
                    tab_personal_corpora.append(line)
                    counter += 1
                    if counter % 10000 == 0:
                        print(counter, " II")
            self._personal_corpora = tab_personal_corpora
            for sentence in tab_personal_corpora:
                self._generate_rhymes_for_sentence(sentence, self._personal_corpora_rhymes)
        return self._personal_corpora

    def get_words_corpora(self):
        if not self._words:
            tab = self.get_personal_corpora_sentences()
            word_tab = []
            for sentence in tab:
                words = sentence.split()[:-1]
                for word in words:
                    word_tab.append(word.lower())
        self._words = word_tab
        
        return self._words


    def get_teddy(self):
        '''
        Makes list of verses from "Pan Tadeusz."
        '''
        if not self._teddy:
            sentences = []
            with open(os.path.join(self.path, '../data/pan_tadeusz.txt'), encoding = 'utf8') as f:
                splitted = [line.rstrip('\n') for line in f]
                for i in range(len(splitted)):
                    sentences.append(splitted[i])
            self._teddy = sentences
            for sentence in sentences:
                self._generate_rhymes_for_sentence(sentence, self._teddy_rhymes)
        return self._teddy

    def get_zemsta(self):
        '''
        Makes list of verses from "Zemsta". Deletes names
        of characters, unecessery spaces and stage
        directors
        '''
        if not self._revenge:
            sentences=[]
            with open(os.path.join(self.path, '../data/zemsta.txt'), encoding = "utf8") as f:
                splitted = [line.rstrip('\n') for line in f]
                for i in range(len(splitted)):
                    verse = splitted[i]
                    if (not verse.startswith("/")) and (len(verse) > 3) and (not verse.isupper()):
                        if verse.startswith(" "):
                            while verse.startswith(" "):
                                verse = verse[1:]
                            sentences.append(verse)
                        elif verse.endswith("—"):
                            sentences.append(verse[:-1])
                        else:
                            sentences.append(verse)
            self._revenge = sentences
            for sentence in sentences:
                self._generate_rhymes_for_sentence(sentence, self._zemsta_rhymes)
                
        return self._revenge

    def _generate_rhymes_for_sentence(self, sentence, container):
        words = self.toolkit.tokenize(sentence)

        for word in words:
            ending = self.toolkit.find_word_ending(word)
            container[ending].append(word)

    @property
    def rhymes_for_zemsta(self):
        return self._zemsta_rhymes

    @property
    def rhymes_for_personal_corpora(self):
        return self._personal_corpora_rhymes

    @property
    def rhymes_for_teddy(self):
        return self._teddy_rhymes

        
