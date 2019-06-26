class LanguageToolkit:
    vowel = ("a", "ą", "e", "ę", "i", "y", "o", "u", "ó")

    def get_syllables(self, word: str) -> list:
        result = []
        syllable = ""
        counter = 0
        while counter < len(word):
            if word[counter] in self.vowel:
                # case: we met the one before last vowel, we add two last letters
                if counter + 1 == len(word) - 1:
                    syllable += word[counter]
                    syllable += word[counter + 1]
                    result.append(syllable)
                    return result
                # case: two vowels next to each other
                if (counter < len(word) - 1) and (word[counter + 1] in self.vowel):
                    syllable += word[counter]
                    syllable += word[counter + 1]
                    result.append(syllable)
                    syllable = ""
                    counter += 2
                else:
                    syllable += word[counter]
                    result.append(syllable)
                    syllable = ""
                    counter += 1
                # case: we met consonant
            else:
                syllable += word[counter]
                counter += 1
        return result

    def count_syllables(self, word: str) -> int:
        return len(self.get_syllables(word))

    def find_word_ending(self, word: str) -> str:
        w_end = ""
        ending = ""
        count_vowel = 0
        if len(self.get_syllables(word)) == 1 or len(word) < 4:
            w_end = word
        for letter in word[::-1]:
            if letter in "/).,(_-:?% 123456789!":
                next
            ending += letter
            if letter in self.vowel:
                count_vowel += 1
                if count_vowel == 2:
                    w_end = ending[::-1]
                    break

        return w_end

    def does_rhyme(self, word_1: str, word_2: str, fst_word_ending: str = None) -> bool:
        w_1_end = fst_word_ending if fst_word_ending else self.find_word_ending(word_1)
        w_2_end = self.find_word_ending(word_2)
        if w_1_end == w_2_end:
            return True
        shorter = w_2_end if len(w_1_end) > len(w_2_end) else w_1_end
        longer = w_1_end if len(w_1_end) > len(w_2_end) else w_2_end
        for i in range(1, len(shorter) - 1):
            shorter = shorter[1:]
            if shorter in longer:
                return True

        return False
