# coding=utf-8
import re
import gensim
import random

# from cymbaline.data import DataProvider

class LanguageToolkit:
    vowel = ("a", "ą", "e", "ę", "i", "y", "o", "u", "ó")
    file_base_vectors = "data/poleval_base_vectors.txt"
    vectors_model = gensim.models.KeyedVectors.load_word2vec_format(file_base_vectors, binary=False)
    vectors_model.init_sims(replace=True)

    def __init__(self):
        # self.data_provider = DataProvider()
        return

    def get_syllables(self, word: str) -> list:
        result = []
        syllable = ""
        character_index = 0
        while character_index < len(word):
            if word[character_index] in self.vowel:
                # case: we met the one before last vowel, we add two last letters
                if character_index + 1 == len(word) - 1:
                    syllable += word[character_index]
                    syllable += word[character_index + 1]
                    result.append(syllable)
                    return result
                # case: two vowels next to each other
                if (character_index < len(word) - 1) and (word[character_index + 1] in self.vowel):
                    syllable += word[character_index]
                    syllable += word[character_index + 1]
                    result.append(syllable)
                    syllable = ""
                    character_index += 2
                else:
                    syllable += word[character_index]
                    result.append(syllable)
                    syllable = ""
                    character_index += 1
                # case: we met consonant
            else:
                syllable += word[character_index]
                character_index += 1
        return result

    def count_syllables(self, word: str) -> int:
        return len(self.get_syllables(word))

    def is_n_syllable(self, word: str, n: int) -> bool:
        return n == self.count_syllables(word)

    def find_word_ending(self, word: str) -> str:
        w_end = ""
        ending = ""
        count_vowel = 0
        if len(self.get_syllables(word)) == 1 or len(word) < 4:
            w_end = word
        for letter in word[::-1]:
            ending += letter
            if letter in self.vowel:
                count_vowel += 1
                if count_vowel == 2:
                    w_end = ending[::-1]
                    break

        return w_end

    def does_rhyme(self, word_1: str, word_2: str, fst_word_ending: str = None) -> bool:
        word_1_ending = fst_word_ending if fst_word_ending else self.find_word_ending(word_1)
        word_2_ending = self.find_word_ending(word_2)
        if word_1_ending == word_2_ending:
            return True
        shorter = word_2_ending if len(word_1_ending) > len(word_2_ending) else word_1_ending
        longer = word_1_ending if len(word_1_ending) > len(word_2_ending) else word_2_ending
        for i in range(1, len(shorter) - 1):
            shorter = shorter[1:]
            if shorter in longer:
                return True

    def tokenize(self, line: str) -> list:
        line = line.lower()
        pattern = r"\s*\w*\s*"
        result = re.findall(pattern, line)
        result = list(filter(lambda y: len(y), map(lambda x: x.strip(), result)))

        return result
    
    def top_related_words(self, words, top_n=20):
        return map(lambda pair: pair[0], self.vectors_model.most_similar(words, topn=top_n))

    def n_syllable_top_related_words(self, syllable_count: int, context_words=None) -> list:
        words = self.top_related_words(words=context_words, top_n=2000)
        words = list(filter(lambda word: self.is_n_syllable(word, syllable_count), words))
        # while len(words) < 10:
        #     number_of_random_verses = 42
        #     random_verses = random.sample(self.data_provider.get_zemsta(), k=number_of_random_verses)
        #     random_sample = ' '.join(random_verses)
        #     random_words = self.tokenize(random_sample)
        #     random_words = list(filter(lambda word: self.is_n_syllable(word, syllable_count), random_words))
        #     words.append(random_words)
        return words


