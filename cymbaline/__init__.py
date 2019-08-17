from cymbaline.connectors import TelegramConnector
from cymbaline.interactions import Interaction


class Bot:
    def deploy(self, target: str = "Production", debug: bool = False):
        print(f"Deploying the bot on {target}")
        if target == "CLI":
            while True:
                user_input = input("> ")
                interaction = Interaction(user_input=user_input)
                bot_response = interaction.get_response()
                print(bot_response)