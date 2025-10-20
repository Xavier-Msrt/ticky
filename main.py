
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    if token is None:
        print('Please provide a token in the .env file (DISCORD_TOKEN)')
        exit()


    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    bot = commands.Bot(command_prefix='!', intents=intents)
    bot.run(token)