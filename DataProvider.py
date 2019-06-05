import numpy as np

class DataProvider:

    def get_dict(self):
        '''
        Make dictionary that contains {word, np.array[vector]}.
        We don't need to know vectors of words shorter than 3
        and that contains characters different that letters.
        '''
        dict_poleval = {}
        counter = 0
        with open('poleval_base_vectors.txt', encoding='utf8') as f:
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
        return dict_poleval

    def get_tab(self):
        '''
        Make list that contains sentences from personal corpora.
        '''
        tab_personal_corpora = []
        counter = 0
        with open('personal_corpora.txt', encoding='utf8') as f:
            for line in f:
                line = line[:-3] + line[-2] #erase spaces and '/n' characters
                tab_personal_corpora.append(line)
                counter += 1
                if counter % 10000 == 0:
                    print(counter, " II")
        return tab_personal_corpora

    def get_words_corpora(self):
        tab = DataProvider()
        tab = tab.get_tab()
        word_tab = []
        for sentence in tab:
            words = sentence.split()[:-1]
            for word in words:
                word_tab.append(word.lower())
        return word_tab


    def get_teddy(self):
        '''
        Makes list of verses from "Pan Tadeusz."
        '''
        sentences = []
        with open('pan_tadeusz.txt', encoding = 'utf8') as f:
            splitted = [line.rstrip('\n') for line in f]
            for i in range(len(splitted)):
                sentences.append(splitted[i])
        return sentences

    def get_revenge(self):
        '''
        Makes list of verses from "Zemsta". Deletes names
        of characters and unecessery spaces and stage
        directors
        '''
        sentences=[]
        with open('zemsta.txt', encoding = "utf8") as f:
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
        return sentences
                     




