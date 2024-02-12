#discord.py
import discord

#my modules
from config import config
import bot.utils.on_ready

if __name__ == "__main__":
    #create new client
    bot = commands.Bot(
        command_prefix = config.command_prefix,
        intents = config.intents
    )

    #start bot
    client.run(TOKEN)

