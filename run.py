from cymbaline import Bot
from cymbaline.data import DataProvider
from cymbaline.language import LanguageToolkit
from cymbaline.generators import HaikuGenerator
from collections import defaultdict


if __name__ == "__main__":
    bot = Bot()
    bot.deploy(target="CLI", debug=True)
