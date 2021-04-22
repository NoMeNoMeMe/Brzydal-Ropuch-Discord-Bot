import discord
from discord.ext import commands
import time
import asyncio

# https://www.youtube.com/watch?v=eFxrnBxpRE4 - simple logs storing

bot = commands.Bot(command_prefix='!')


class Logs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Logs(bot))
