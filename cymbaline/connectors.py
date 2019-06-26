from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class TelegramConnector:
    def __init__(self, bot_token, answer_function):
        self.updater = Updater(bot_token)
        self.answer_function = answer_function

    def run_bot(self):
        dp = self.updater.dispatcher
        dp.add_handler(MessageHandler(Filters.text, self.answer))
        self.updater.start_polling()
        self.updater.idle()

    def echo(self, bot, update):
        update.message.reply_text(update.message.text)

    def answer(self, bot, update):
        update.message.reply_text(self.answer_function(update.message.text))
