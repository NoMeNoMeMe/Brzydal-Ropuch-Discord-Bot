import discord
from discord.ext import commands
import time
import asyncio

# https://www.youtube.com/watch?v=eFxrnBxpRE4 - simple logs storing

client = commands.Bot(command_prefix='.')


class Logs(commands.Cog):

    def __init__(self, client):
        self.client = client



def setup(client):
    client.add_cog(Logs(client))
