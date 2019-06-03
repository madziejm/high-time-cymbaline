import numpy as np

class DataProvider:


    def get_dict(self):
        dict_poleval = {}
        counter = 0
        with open('poleval_base_vectors.txt', encoding='utf8') as f:
            f.readline()
            for line in f:
                L = line.split()
                doc = [float(s) for s in L[1:]]
                vec = np.array(doc, dtype='single')
                dict_poleval[L[0]] = vec
                counter += 1
                if counter % 10000 == 0:
                    print(counter, " I")
        return dict_poleval

    def get_tab(self):
        tab_personal_corpora = []
        counter = 0
        with open('personal_corpora.txt', encoding='utf8') as f:
            for line in f:
                tab_personal_corpora.append(line)
                counter += 1
                if counter % 10000 == 0:
                    print(counter, " II")
        return tab_personal_corpora

dict = DataProvider()
tab = DataProvider()
dict = dict.get_dict()
tab = tab.get_tab()


