from cymbaline.generators import HaikuGenerator
from cymbaline.language import LanguageToolkit
from cymbaline.data import DataProvider

class Interaction:
    def __init__(self, user_input):
        self.user_input = user_input
        self._choice = None
        self._values = None
        self.toolkit = LanguageToolkit()
        self.dataprovider = DataProvider()

    def determine_best_response(self):
        if self.user_input.startswith("napisz mi haiku o:"):
            self._choice = "haiku"
            self._values = self.user_input[19:].split(",")
            self._values = list(map(lambda x: x.strip(), self._values))
        if self.user_input.startswith("znajdz mi rym do:"):
            self._choice = "find_rhyme"
            self._values = self.user_input[18:].strip()
        if self.user_input.startswith("podziel mi na sylaby:"):
            self._choice = "get_syllables"
            self._values = self.user_input[22:].strip()
        #if self.user_input.startswith("")

    def get_response(self):
        if not self._choice:
            self.determine_best_response()
        
        if self._choice:
            action = getattr(self, f"perform_{self._choice}")
        
            return action()

        return "Nie rozumiem!"

    def perform_haiku(self):
        hg = HaikuGenerator(self._values)

        return hg.generate()

    def perform_find_rhyme(self):
        rhymes = self.dataprovider.rhymes_for_personal_corpora[self._values]

        return rhymes

    def perform_get_syllables(self):
        syllables = self.toolkit.get_syllables(self._values)

        return " ".join(syllables)