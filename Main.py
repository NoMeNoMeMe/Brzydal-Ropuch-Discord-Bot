# -*- coding: utf-8 -*-

import discord
from discord.ext import commands, tasks
import json
import secrets
import os


client = commands.Bot(command_prefix='.')
statuses = open('statusy.txt', 'r', encoding='utf-8')
all_statuses = statuses.readlines()
statuses.close()


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded {filename[:-3]}')


@client.event
async def on_ready():
    change_status.start()
    print('Brzydal Ropuch przejmuje zbrodniczy reżim')


@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(secrets.choice(all_statuses)))


@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    """(cog_name)"""
    client.load_extension(f'cogs.{extension}')
    print(f'{extension} loaded successfully')


@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    """(cog_name)"""
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(f'{extension} reloaded successfully')


@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    """(cog_name)"""
    client.unload_extension(f'cogs.{extension}')
    print(f'{extension} unloaded successfully')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Nie znalazłem takiej komendy, lepiej zapytaj Kurową')


@client.command()
@commands.has_permissions(administrator=True)
async def ping(ctx):
    await ctx.send(f'Mam {round(client.latency * 1000)}ms opóźnienia...')
    print(f'Latency: {round(client.latency * 1000)}ms')


# Brzudal Ropuch
client.run('NzA2NTkyNTQwNDYzMzMzNTA2.Xq8kcA.7NPC_c_P6M8PYmsfqVQ53v85I28')

# Test Bot
# client.run('NzA1NDMwNzUyOTc1NjUwODI2.XrEoSg.TOTSUa3eNg4Xtq_16ggymDFUfXc')

